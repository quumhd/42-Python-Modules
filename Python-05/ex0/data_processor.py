#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._buffer: list[tuple[int, str]] = []
        self._next_rank: int = 1

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._buffer:
            raise IndexError("No ingested data available")
        return self._buffer.pop(0)

    def _push(self, value: str) -> None:
        self._buffer.append((self._next_rank, value))
        self._next_rank += 1


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) and
                       not isinstance(item, bool) for item in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._push(str(item))
        else:
            self._push(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("TextProcessor expects str or list[str]")
        if isinstance(data, list):
            for item in data:
                self._push(item)
        else:
            self._push(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return (
                "log_level" in data and
                "log_message" in data and
                isinstance(data["log_level"], str) and
                isinstance(data["log_message"], str)
            )
        if isinstance(data, list):
            return all(isinstance(item, dict) and self.validate(item)
                       for item in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError(
                "LogProcessor expects dict[str, str] or list[dict[str, str]]"
            )
        if isinstance(data, list):
            for item in data:
                self._push(self._format_log(item))
        else:
            self._push(self._format_log(data))

    def _format_log(self, data: dict[str, str]) -> str:
        level = data["log_level"].strip()
        message = data["log_message"].strip()
        return f"{level}: {message}"


def data_processor():
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")  # type: ignore[arg-type]
    except Exception as error:
        print(f"Got exception: {error}")

    numeric_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    numeric.ingest(numeric_data)
    print("Extracting 3 values...")
    for i in range(3):
        _, value = numeric.output()
        print(f"Numeric value {i}: {value}")
    print()
    print("Testing Text Processor...")
    print(f"Trying to validate input '42': {text.validate(42)}")
    text_data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}")
    text.ingest(text_data)
    print("Extracting 1 value...")
    _, text_value = text.output()
    print(f"Text value 0: {text_value}")
    print()
    print("Testing Log Processor...")
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR\n", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {log_data}")
    log.ingest(log_data)
    print("Extracting 2 values...")
    for i in range(2):
        _, entry = log.output()
        print(f"Log entry {i}: {entry}")


if __name__ == "__main__":
    data_processor()
