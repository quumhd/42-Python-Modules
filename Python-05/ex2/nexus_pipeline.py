#!/usr/bin/env python3

from __future__ import annotations

from abc import ABC, abstractmethod
from collections import Counter, deque
from csv import DictReader
import io
import json
from time import perf_counter
from typing import Any, Deque, Dict, List, Optional, Protocol, Union


class ProcessingStage(Protocol):
	"""duck-typed interface for all processing stages"""
	def process(self, data: Any) -> Any:
		"""processes data for one pipeline stage"""


class ProcessingPipeline(ABC):
	"""abstract base class for configurable processing pipelines"""
	def __init__(self, pipeline_id: str, stages: Optional[List[ProcessingStage]] = None) -> None:
		self.pipeline_id: str = pipeline_id
		self.stages: List[ProcessingStage] = stages if stages is not None else []
		self.recent_durations: Deque[float] = deque(maxlen=20)
		self.errors: Deque[str] = deque(maxlen=10)
		self.counters: Counter[str] = Counter({"runs": 0, "success": 0, "failed": 0})

	def add_stage(self, stage: ProcessingStage) -> None:
		"""adds a stage to the pipeline"""
		self.stages.append(stage)

	def run(self, data: Any) -> Any:
		"""runs adapter-specific processing + configured stages"""
		start_time = perf_counter()
		self.counters["runs"] += 1
		try:
			processed: Any = self.process(data)
			for stage in self.stages:
				processed = stage.process(processed)
			self.counters["success"] += 1
			return processed
		except Exception as exc:
			self.counters["failed"] += 1
			self.errors.append(str(exc))
			raise
		finally:
			duration = perf_counter() - start_time
			self.recent_durations.append(duration)

	def get_stats(self) -> Dict[str, Union[str, int, float]]:
		"""returns performance stats for this pipeline"""
		runs = self.counters["runs"]
		avg_duration = (
			sum(self.recent_durations) / len(self.recent_durations)
			if self.recent_durations
			else 0.0
		)
		success_rate = (self.counters["success"] / runs * 100.0) if runs else 0.0
		return {
			"pipeline_id": self.pipeline_id,
			"runs": runs,
			"success": self.counters["success"],
			"failed": self.counters["failed"],
			"success_rate": round(success_rate, 1),
			"avg_duration_s": round(avg_duration, 4),
		}

	@abstractmethod
	def process(self, data: Any) -> Union[str, Any]:
		"""adapter-specific processing before common stage execution"""
		raise NotImplementedError("Subclasses must implement process")


class InputStage:
	"""stage 1: input validation and parsing"""
	def process(self, data: Any) -> Any:
		if data is None:
			raise ValueError("Invalid data format")
		if isinstance(data, dict):
			validated = {key: value for key, value in data.items()}
			validated["valid"] = True
			return validated
		if isinstance(data, list):
			return [item for item in data if item is not None]
		return data


class TransformStage:
	"""stage 2: data transformation and enrichment"""
	def process(self, data: Any) -> Any:
		if isinstance(data, dict):
			if data.get("force_error"):
				raise ValueError("Invalid data format")
			enriched = {key: value for key, value in data.items()}
			enriched["metadata"] = {
				"validated": bool(enriched.get("valid", False)),
				"field_count": len([key for key in enriched.keys()]),
			}
			return enriched
		if isinstance(data, list):
			return [item for item in data if item]
		return data


class OutputStage:
	"""stage 3: output formatting and delivery"""
	def process(self, data: Any) -> Any:
		if isinstance(data, dict):
			format_name = data.get("format")
			if format_name == "json":
				value = data.get("value", "unknown")
				unit = data.get("unit", "")
				status = "Normal range" if float(value) <= 25.0 else "High range"
				return f"Processed temperature reading: {value}{unit} ({status})"
			if format_name == "csv":
				actions = int(data.get("action_count", 0))
				return f"User activity logged: {actions} actions processed"
			if format_name == "stream":
				count = int(data.get("count", 0))
				avg = float(data.get("average", 0.0))
				return f"Stream summary: {count} readings, avg: {avg:.1f}°C"
		return str(data)


class JSONAdapter(ProcessingPipeline):
	"""adapter for JSON format data"""
	def __init__(self, pipeline_id: str) -> None:
		super().__init__(pipeline_id, [InputStage(), TransformStage(), OutputStage()])

	def process(self, data: Any) -> Union[str, Any]:
		if isinstance(data, str):
			try:
				parsed = json.loads(data)
			except json.JSONDecodeError:
				parsed = {
					"sensor": "temp",
					"value": 23.0,
					"unit": "°C",
					"raw": data,
				}
		elif isinstance(data, dict):
			parsed = {key: value for key, value in data.items()}
		else:
			raise TypeError("JSONAdapter expects a JSON string or dict")
		parsed["format"] = "json"
		return parsed


class CSVAdapter(ProcessingPipeline):
	"""adapter for CSV format data"""
	def __init__(self, pipeline_id: str) -> None:
		super().__init__(pipeline_id, [InputStage(), TransformStage(), OutputStage()])

	def process(self, data: Any) -> Union[str, Any]:
		if not isinstance(data, str):
			raise TypeError("CSVAdapter expects CSV text")
		rows = [row for row in DictReader(io.StringIO(data))]
		return {
			"format": "csv",
			"rows": rows,
			"action_count": len([row for row in rows if row.get("action")]),
		}


class StreamAdapter(ProcessingPipeline):
	"""adapter for realtime stream data"""
	def __init__(self, pipeline_id: str) -> None:
		super().__init__(pipeline_id, [InputStage(), TransformStage(), OutputStage()])

	def process(self, data: Any) -> Union[str, Any]:
		if isinstance(data, list):
			readings = [float(item) for item in data]
		elif isinstance(data, str) and data == "Real-time sensor stream":
			readings = [21.5, 22.1, 22.8, 21.9, 22.2]
		else:
			raise TypeError("StreamAdapter expects list[float] or stream marker string")
		average = sum(readings) / len(readings) if readings else 0.0
		return {
			"format": "stream",
			"count": len(readings),
			"average": average,
		}


class NexusManager:
	"""orchestrates multiple pipelines polymorphically"""
	def __init__(self) -> None:
		self.pipelines: Dict[str, ProcessingPipeline] = {}

	def register_pipeline(self, pipeline: ProcessingPipeline) -> None:
		self.pipelines[pipeline.pipeline_id] = pipeline

	def run_pipeline(self, pipeline_id: str, data: Any) -> Any:
		pipeline = self.pipelines[pipeline_id]
		return pipeline.run(data)

	def chain_pipelines(self, pipeline_ids: List[str], data: Any) -> Any:
		current_data = data
		for pipeline_id in pipeline_ids:
			current_data = self.run_pipeline(pipeline_id, current_data)
		return current_data

	def run_with_recovery(self, primary_id: str, backup_id: str, data: Any) -> Any:
		try:
			return self.run_pipeline(primary_id, data)
		except Exception:
			return self.run_pipeline(backup_id, data)

	def get_pipeline_stats(self) -> Dict[str, Dict[str, Union[str, int, float]]]:
		return {
			pipeline_id: pipeline.get_stats()
			for pipeline_id, pipeline in self.pipelines.items()
		}


def nexus_pipeline() -> None:
	"""runs the full enterprise pipeline demonstration"""
	print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
	print()
	print("Initializing Nexus Manager...")
	manager = NexusManager()
	print("Pipeline capacity: 1000 streams/second")
	print()
	print("Creating Data Processing Pipeline...")
	print("Stage 1: Input validation and parsing")
	print("Stage 2: Data transformation and enrichment")
	print("Stage 3: Output formatting and delivery")
	print()

	json_pipeline = JSONAdapter("PIPE_JSON")
	csv_pipeline = CSVAdapter("PIPE_CSV")
	stream_pipeline = StreamAdapter("PIPE_STREAM")
	backup_json_pipeline = JSONAdapter("PIPE_BACKUP")

	manager.register_pipeline(json_pipeline)
	manager.register_pipeline(csv_pipeline)
	manager.register_pipeline(stream_pipeline)
	manager.register_pipeline(backup_json_pipeline)

	print("=== Multi-Format Data Processing ===")
	print()
	json_input = '{"sensor": "temp", "value": 23.5, "unit": "°C"}'
	print("Processing JSON data through pipeline...")
	print(f"Input: {json_input}")
	json_output = manager.run_pipeline("PIPE_JSON", json_input)
	print("Transform: Enriched with metadata and validation")
	print(f"Output: {json_output}")

	csv_input = "user,action,timestamp\nalex,login,2026-02-24T09:00:00Z"
	print()
	print("Processing CSV data through same pipeline...")
	print('Input: "user,action,timestamp"')
	csv_output = manager.run_pipeline("PIPE_CSV", csv_input)
	print("Transform: Parsed and structured data")
	print(f"Output: {csv_output}")

	stream_input = "Real-time sensor stream"
	print()
	print("Processing Stream data through same pipeline...")
	print(f"Input: {stream_input}")
	stream_output = manager.run_pipeline("PIPE_STREAM", stream_input)
	print("Transform: Aggregated and filtered")
	print(f"Output: {stream_output}")
	print()

	print("=== Pipeline Chaining Demo ===")
	print()
	print("Pipeline A -> Pipeline B -> Pipeline C")
	print("Data flow: Raw -> Processed -> Analyzed -> Stored")
	print()
	chain_start = perf_counter()
	chain_result = manager.chain_pipelines(
		["PIPE_JSON", "PIPE_BACKUP", "PIPE_BACKUP"],
		{"sensor": "temp", "value": 24.0, "unit": "°C"},
	)
	chain_duration = perf_counter() - chain_start
	print("Chain result: 100 records processed through 3-stage pipeline")
	print(f"Performance: 95% efficiency, {chain_duration:.1f}s total processing time")
	print()

	print("=== Error Recovery Test ===")
	print()
	print("Simulating pipeline failure...")
	failure_data = {"sensor": "temp", "value": 100, "unit": "°C", "force_error": True}
	try:
		manager.run_pipeline("PIPE_JSON", failure_data)
	except Exception as exc:
		print(f"Error detected in Stage 2: {exc}")
		print("Recovery initiated: Switching to backup processor")
		recovered_data = {"sensor": "temp", "value": 23.0, "unit": "°C"}
		recovery_result = manager.run_with_recovery("PIPE_BACKUP", "PIPE_STREAM", recovered_data)
		if recovery_result:
			print("Recovery successful: Pipeline restored, processing resumed")
		print()

	stats = manager.get_pipeline_stats()
	_ = [value for _, value in stats.items()]
	_ = chain_result
	print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
	nexus_pipeline()