#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol


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

    def add_element(self, value: str) -> None:
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
                self.add_element(str(item))
        else:
            self.add_element(str(data))


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
                self.add_element(item)
        else:
            self.add_element(data)


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
                self.add_element(self._format_log(item))
        else:
            self.add_element(self._format_log(data))

    def _format_log(self, data: dict[str, str]) -> str:
        level = data["log_level"].strip()
        message = data["log_message"].strip()
        return f"{level}: {message}"


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CsvPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> str:
        csv_data = ""
        for item in data:
            _, temp = item
            if csv_data == "":
                csv_data = str(temp)
            else:
                csv_data = csv_data + "," + str(temp)
        return "CSV Output:\n" + csv_data


class JsonPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> str:
        json_data = ""
        for item in data:
            count_int, temp = item
            count = '"item_' + str(count_int) + '": '
            temp = '"' + str(temp) + '", '
            json_data = json_data + count + str(temp)
        json_data = "{" + json_data + "}"
        return "JSON Output:\n" + json_data


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []
        self._processed_count: dict[int, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)
        self._processed_count[id(proc)] = 0

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            handled = False
            for processor in self._processors:
                if processor.validate(item):
                    processor.ingest(item)
                    proc_id = id(processor)
                    if isinstance(item, list):
                        count = len(item)
                    else:
                        count = 1
                    self._processed_count[proc_id] += count
                    handled = True
                    break
            if not handled:
                print(
                    "DataStream error - Can't process "
                    f"element in stream: {item}"
                )

    def output_pipline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            data = list()
            for _ in range(nb):
                try:
                    data.append(proc.output())
                except IndexError:
                    pass
            print(plugin.process_output(data))  # type: ignore

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for processor in self._processors:
            name = processor.__class__.__name__.replace(
                "Processor", " Processor"
            )
            total_processed = self._processed_count.get(id(processor), 0)
            remaining = len(processor._buffer)
            print(
                f"{name}: total {total_processed} items processed, "
                f"remaining {remaining} on processor"
            )


def remove_element(processor: DataProcessor, count: int) -> None:
    for _ in range(count):
        try:
            processor.output()
        except IndexError:
            return


def data_pipline():

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    stream_router = DataStream()
    mixed_stream = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    mixed_stream2 = [
        21,
        [
            'I love AI', 'LLMs are wonderful', 'Stay healthy'
        ],
        [
            {
                'log_level': 'ERROR',
                'log_message': '500 server crash'
            },
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
                }
            ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]

    print("=== Code Nexus - Data Pipline ===\n")
    print("Initialize Data Stream...\n")
    stream_router.print_processors_stats()
    print()
    print("Registering Processors\n")
    stream_router.register_processor(numeric)
    stream_router.register_processor(text)
    stream_router.register_processor(log)
    stream_router.process_stream(mixed_stream)
    print(f"Send first batch of data on stream: {mixed_stream}")
    print()
    stream_router.print_processors_stats()
    print()
    print("Send 3 processed data from each processor to a CSV plugin:")
    stream_router.output_pipline(3, CsvPlugin())
    print()
    stream_router.print_processors_stats()
    print()
    stream_router.process_stream(mixed_stream2)
    print(f"Send another batch of data: {mixed_stream2}\n")
    stream_router.print_processors_stats()
    print()
    print("Send 5 processed data from each processor to a JSON plugin:")
    stream_router.output_pipline(5, JsonPlugin())
    print()
    stream_router.print_processors_stats()


if __name__ == "__main__":
    data_pipline()
