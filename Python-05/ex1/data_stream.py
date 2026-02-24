#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
	"""abstract base class for data streams"""
	@abstractmethod
	def process_batch(self, data_batch: List[Any]) -> str:
		"""processes a batch of data"""
		raise NotImplementedError("Subclasses must implement this method")

	def filter_data(self, data: List[Any], criteria: Optional[str]=None) -> List[Any]:
		"""filters data based on criteria"""
		if criteria is None:
			return data
		has_criteria = []
		for item in data:
			if criteria in str(item):
				has_criteria.append(item)
		return has_criteria

	def get_stats(self) -> Dict[str, Union[str, int, float]]:
		"""returns statistics about the data stream"""
		return {"status": "No statistics available"}


class SensorStream(DataStream):
	"""data stream for sensor data"""
	def __init__(self, sensor_id: str):
		self.sensor_id = sensor_id
		self.data = []

	def process_batch(self, data_batch: List[float]) -> str:
		"""processes a batch of sensor data and returns average value"""
		self.data.extend(data_batch)
		if not self.data:
			return "No data to process"
		avg_value = sum(self.data) / len(self.data)
		return f"Sensor {self.sensor_id} - Average Value: {avg_value:.2f}"

	def filter_data(self, data: List[float], criteria: Optional[str]=None) -> List[float]:
		"""filters sensor data based on criteria (e.g., threshold)"""
		if criteria is None:
			return data
		try:
			threshold = float(criteria)
			return [x for x in data if x > threshold]
		except ValueError:
			return data

	def get_stats(self) -> Dict[str, Union[str, int, float]]:
		"""returns statistics about the sensor data stream"""
		if not self.data:
			return {"sensor_id": self.sensor_id, "count": 0, "average": 0.0}
		return {
			"sensor_id": self.sensor_id,
			"count": len(self.data),
			"average": sum(self.data) / len(self.data)
		}


class TransactionStream(DataStream):
	"""data stream for transaction data"""
	def __init__(self, stream_id: str):
		self.stream_id = stream_id
		self.transactions = []

	def process_batch(self, data_batch: List[Dict[str, Any]]) -> str:
		"""processes a batch of transactions and returns total amount"""
		self.transactions.extend(data_batch)
		total_amount = sum(txn.get("amount", 0) for txn in self.transactions)
		return f"Transaction Stream {self.stream_id} - Total Amount: {total_amount:.2f}"

	def filter_data(self, data: List[Dict[str, Any]], criteria: Optional[str]=None) -> List[Dict[str, Any]]:
		"""filters transactions based on criteria (e.g., minimum amount)"""
		if criteria is None:
			return data
		try:
			min_amount = float(criteria)
			return [txn for txn in data if txn.get("amount", 0) > min_amount]
		except ValueError:
			return data

	def get_stats(self) -> Dict[str, Union[str, int, float]]:
		"""returns statistics about the transaction data stream"""
		total_amount = sum(txn.get("amount", 0) for txn in self.transactions)
		return {
			"stream_id": self.stream_id,
			"transaction_count": len(self.transactions),
			"total_amount": total_amount
		}


class EventStream(DataStream):
	"""data stream for event data"""
	def __init__(self, event_type: str):
		self.event_type = event_type
		self.events = []

	def process_batch(self, data_batch: List[Dict[str, Any]]) -> str:
		"""processes a batch of events and returns count of events"""
		self.events.extend(data_batch)
		return f"Event Stream {self.event_type} - Event Count: {len(self.events)}"

	def filter_data(self, data: List[Dict[str, Any]], criteria: Optional[str]=None) -> List[Dict[str, Any]]:
		"""filters events based on criteria (e.g., event severity)"""
		if criteria is None:
			return data
		return [event for event in data if event.get("severity") == criteria]

	def get_stats(self) -> Dict[str, Union[str, int]]:
		"""returns statistics about the event data stream"""
		return {
			"event_type": self.event_type,
			"event_count": len(self.events)
		}


class StreamProcessor:
	"""polymorphic stream processor that handles multiple stream types"""
	def __init__(self):
		self.streams: List[DataStream] = []

	def register_stream(self, stream: DataStream) -> None:
		"""register a new stream for processing"""
		self.streams.append(stream)

	def process_all_streams(self, data_batches: List[tuple]) -> List[str]:
		"""process multiple batches through their respective streams polymorphically"""
		results = []
		for idx, (stream, batch) in enumerate(data_batches):
			try:
				if not isinstance(stream, DataStream):
					results.append(f"Batch {idx}: Error - Not a valid DataStream")
					continue
				result = stream.process_batch(batch)
				results.append(f"Batch {idx}: {result}")
			except Exception as e:
				results.append(f"Batch {idx}: Error processing stream - {e}")
		return results

	def get_all_stats(self) -> Dict[str, Any]:
		"""retrieve statistics from all registered streams"""
		stats = {}
		for idx, stream in enumerate(self.streams):
			try:
				stream_stats = stream.get_stats()
				stream_name = stream.__class__.__name__
				stats[f"{stream_name}_{idx}"] = stream_stats
			except Exception as e:
				stats[f"Stream_{idx}_Error"] = str(e)
		return stats

	def filter_all_streams(self, criteria: str) -> Dict[str, List[Any]]:
		"""filter data across all registered streams"""
		filtered = {}
		for idx, stream in enumerate(self.streams):
			try:
				if hasattr(stream, 'data'):
					filtered_data = stream.filter_data(stream.data, criteria)
				elif hasattr(stream, 'transactions'):
					filtered_data = stream.filter_data(stream.transactions, criteria)
				elif hasattr(stream, 'events'):
					filtered_data = stream.filter_data(stream.events, criteria)
				else:
					filtered_data = []
				stream_name = stream.__class__.__name__
				filtered[f"{stream_name}_{idx}"] = filtered_data
			except Exception as e:
				filtered[f"Stream_{idx}_Error"] = str(e)
		return filtered


def data_stream() -> None:
	"""demonstrates polymorphic data stream processing"""
	print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
	print("Initializing Sensor Stream...")
	sensor_stream = SensorStream("SENSOR_001")
	print("Stream ID: SENSOR_001, Type: Environmental Data")
	print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
	raw_sensor_batch_1 = ["temp:22.5", "humidity:65", "pressure:1013"]
	temp_batch_1 = [float(item.split(":")[1]) for item in raw_sensor_batch_1 if item.startswith("temp:")]
	sensor_stream.process_batch(temp_batch_1)
	avg_temp = sum(temp_batch_1) / len(temp_batch_1)
	print(f"Sensor analysis: {len(raw_sensor_batch_1)} readings processed, avg temp: {avg_temp:.1f}°C")
	print()
	
	print("Initializing Transaction Stream...")
	transaction_stream = TransactionStream("TRANS_001")
	print("Stream ID: TRANS_001, Type: Financial Data")
	print("Processing transaction batch: [buy:100, sell:150, buy:75]")
	transaction_batch_1 = [
		{"type": "buy", "amount": 100.0},
		{"type": "sell", "amount": 150.0},
		{"type": "buy", "amount": 75.0}
	]
	transaction_stream.process_batch(transaction_batch_1)
	net_flow = sum(txn["amount"] if txn["type"] == "buy" else -txn["amount"] for txn in transaction_batch_1)
	print(f"Transaction analysis: {len(transaction_batch_1)} operations, net flow: {net_flow:+.0f} units")
	print()
	
	print("Initializing Event Stream...")
	event_stream = EventStream("SYSTEM_EVENTS")
	print("Stream ID: EVENT_001, Type: System Events")
	print("Processing event batch: [login, error, logout]")
	event_batch_1 = [
		{"event": "login", "severity": "low"},
		{"event": "error", "severity": "high"},
		{"event": "logout", "severity": "low"}
	]
	event_stream.process_batch(event_batch_1)
	error_count = sum(1 for event in event_batch_1 if event["severity"] == "high")
	print(f"Event analysis: {len(event_batch_1)} events, {error_count} error detected")
	print()
	
	print("=== Polymorphic Stream Processing ===")
	processor = StreamProcessor()
	processor.register_stream(sensor_stream)
	processor.register_stream(transaction_stream)
	processor.register_stream(event_stream)
	
	print("Processing mixed stream types through unified interface...")
	print()
	
	raw_sensor_batch_poly_1 = ["temp:24.0", "temp:25.0"]
	temp_batch_poly_1 = [float(item.split(":")[1]) for item in raw_sensor_batch_poly_1 if item.startswith("temp:")]
	transaction_batch_poly_1 = [
		{"type": "buy", "amount": 150.0},
		{"type": "sell", "amount": 100.0},
		{"type": "buy", "amount": 125.0},
		{"type": "buy", "amount": 75.0}
	]
	event_batch_poly_1 = [
		{"event": "warning", "severity": "high"},
		{"event": "info", "severity": "low"},
		{"event": "critical", "severity": "high"}
	]

	processor.process_all_streams([
		(sensor_stream, temp_batch_poly_1),
		(transaction_stream, transaction_batch_poly_1),
		(event_stream, event_batch_poly_1)
	])

	sensor_readings = len(temp_batch_poly_1)
	transaction_ops = len(transaction_batch_poly_1)
	event_count = len(event_batch_poly_1)
	
	print("Batch 1 Results:")
	print(f"- Sensor data: {sensor_readings} readings processed")
	print(f"- Transaction data: {transaction_ops} operations processed")
	print(f"- Event data: {event_count} events processed")
	print()
	
	sensor_alerts = sensor_stream.filter_data(sensor_stream.data, "23")
	transaction_filtered = transaction_stream.filter_data(transaction_stream.transactions, "120")

	critical_alerts = len(sensor_alerts)
	large_transactions = len(transaction_filtered)
	alert_label = "alert" if critical_alerts == 1 else "alerts"
	transaction_label = "transaction" if large_transactions == 1 else "transactions"
	
	print("Stream filtering active: High-priority data only")
	print(f"Filtered results: {critical_alerts} critical sensor {alert_label}, {large_transactions} large {transaction_label}")
	print()
	print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
	data_stream()
