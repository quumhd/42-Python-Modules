#!/usr/bin/env python3


from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
	"""abstract base class for data stream processing"""
	@abstractmethod
	def process(self, data: Any) -> str:
		"""processes a data stream"""
		pass

	@abstractmethod
	def validate(self, data: Any) -> bool:
		"""validates a data stream"""
		pass

	def format_output(self, data: Any) -> str:
		"""formats the output of a data stream"""
		return f"Processed data: {data}"


class NumericProcessor(DataProcessor):
	"""data processor for numeric data streams"""
	def process(self, data: Any) -> str:
		"""processes numeric data stream and returns sum, average, and count"""
		try:
			if not self.validate(data):
				raise ValueError("Input contains non numeric values")
			sume = sum(data)
			agv = sume / len(data)
			length = len(data)
			return self.format_output([sume, agv, length])
		except ValueError as e:
			return f"Error processing numeric data: {e}"

	def validate(self, data: Any) -> bool:
		"""validates that the input is a list of numeric values"""
		return isinstance(data, list) and all(isinstance(x, (int, float)) for x in data)

	def format_output(self, data: Any) -> str:
		"""formats the output for numeric data stream processing"""
		return f"Processed {data[2]} values, sum={data[0]}, avg={data[1]}"
	
class TextProcessor(DataProcessor):
	"""data processor for text data streams"""
	def process(self, data: Any) -> str:
		"""processes text data stream and returns character count and word count"""
		try:
			if not self.validate(data):
				raise ValueError("Input is not valid text data")
			char_count = len(data)
			word_count = len(data.split())
			return self.format_output([char_count, word_count])
		except ValueError as e:
			return f"Error processing text data: {e}"

	def validate(self, data: Any) -> bool:
		"""validates that the input is a string"""
		return isinstance(data, str)

	def format_output(self, data: Any) -> str:
		"""formats the output for text data stream processing"""
		return f"Processed Text: {data[0]} characters, {data[1]} words"
	
class LogProcessor(DataProcessor):
	"""data processor for log data streams"""
	def process(self, data: Any) -> str:
		try:
			if not self.validate(data):
				raise ValueError("Input is not valid log data")
			return self.format_output(data)
		except ValueError as e:
			return f"Error processing log data: {e}"

	def validate(self, data: Any) -> bool:
		return isinstance(data, str) and "ERROR" in data

	def format_output(self, data: Any) -> str:
		return f"[Alert] Error level dected: {' '.join(data.split()[1:])}"


class StreamProcessor:
	"""main class for demonstrating polymorphic data stream processing"""
	def __init__(self):
		self.processors = [
		NumericProcessor(),
		TextProcessor(),
		LogProcessor()
		]
		
	def process_stream(self, data: Any) -> None:
		"""processes a data stream through all processors"""
		for processor in self.processors:
			if processor.validate(data):
				print(processor.process(data))


def stream_processor() -> None:
	"""demonstrates polymorphic data stream processing"""
	print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

	print()

	print("Initializing Numeric Processor...")
	numeric_processor = NumericProcessor()
	numeric_data = [1, 2, 3, 4, 5]
	print(f"Processing data: {numeric_data}")
	print(f"Validation result: {numeric_processor.validate(numeric_data)}")
	print("Output:", numeric_processor.process(numeric_data))
	
	print()

	print("Initializing Text Processor...")
	text_processor = TextProcessor()
	text_data = "Hello Nexus World"
	print(f"Processing data: {text_data}")
	print(f"Validation result: {text_processor.validate(text_data)}")
	print("Output:", text_processor.process(text_data))

	print()

	print("Initializing Log Processor...")
	log_processor = LogProcessor()
	log_data = "ERROR: Connection timeout"
	print(f"Processing data: {log_data}")
	print(f"Validation result: {log_processor.validate(log_data)}")
	print("Output:", log_processor.process(log_data))

	print()

	processor = StreamProcessor()
	print("\n=== Polymorhpic Processing Demo ===")
	print()
	print("Processing multiple data types through same interface...\n")
	processor.process_stream(numeric_data)
	processor.process_stream(text_data)
	processor.process_stream(log_data)


if __name__ == "__main__":
	stream_processor()
