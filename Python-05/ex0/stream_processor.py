#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Optional


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for NumericProcessor")
        return (str(len(data)) + " " + str(sum(data)) + " " +
                str(sum(data) / len(data)))

    def validate(self, data: Any) -> bool:
        return all(isinstance(x, (int, float)) for x in data)

    def format_output(self, result: str) -> str:
        data: List[str] = result.split()
        return (f"Processed {data[0]} numeric values, "
                f"sum={data[1]}, avg={data[2]}")


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for TextProcessor")
        return str(len(data)) + " " + str(len(data.split()))

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        data: List[str] = result.split()
        return f"Processed text: {data[0]} characters, {data[1]} words"


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for LogProcessor")
        return f"{data}"

    def validate(self, data: Any) -> bool:
        return isinstance(data, dict)

    def format_output(self, result: str) -> str:
        cleaned = result.replace("{", "").replace("}", "")
        cleaned = cleaned.replace("'", "").replace('"', "")
        if cleaned.startswith("ERROR:"):
            return f"[ALERT] {cleaned}"
        return f"{cleaned}"


def UniversalProcessor(data: Any) -> Optional[str]:
    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    if numeric_processor.validate(data):
        return numeric_processor.format_output(numeric_processor.process(data))
    elif text_processor.validate(data):
        return text_processor.format_output(text_processor.process(data))
    elif log_processor.validate(data):
        return log_processor.format_output(log_processor.process(data))
    else:
        return None


def stream_processor():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    numeric_processor = NumericProcessor()
    numeric_data = [1, 2, 3, 4, 5]
    if numeric_processor.validate(numeric_data):
        print(f"Processing data: {numeric_data}")
        print("Validation: Numeric data verified")
        processed = numeric_processor.process(numeric_data)
        print(f"Output: {numeric_processor.format_output(processed)}\n")
    else:
        print("Invalid data for Numeric Processor")

    print("Initializing Text Processor...")
    text_processor = TextProcessor()
    text_data = "Hello Nexus World"
    if text_processor.validate(text_data):
        print(f"Processing data: {text_data}")
        print("Validation: Text data verified")
        processed = text_processor.process(text_data)
        print(f"Output: {text_processor.format_output(processed)}\n")
    else:
        print("Invalid data for Text Processor")

    print("Initializing Log Processor...")
    log_processor = LogProcessor()
    log_data = {"ERROR": "Connection timeout"}
    if log_processor.validate(log_data):
        print(f"Processing data: {log_data}")
        print("Validation: Log data verified")
        processed = log_processor.process(log_data)
        print(f"Output: {log_processor.format_output(processed)}\n")
    else:
        print("Invalid data for Log Processor")

    print("\n=== Polymarphic Processing Demo ===\n")
    result = UniversalProcessor(numeric_data)
    print(f"Result 1: {result}")
    result = UniversalProcessor(text_data)
    print(f"Result 2: {result}")
    result = UniversalProcessor(log_data)
    print(f"Result 3: {result}")
    print("\nFoundation systems online. Nexus ready for advaced streams.")


if __name__ == "__main__":
    stream_processor()
