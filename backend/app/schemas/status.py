from enum import Enum


class Status(Enum):
    QUEUE = "queued to be processed"
    PROCESSIG = "file processing"
    PROCESSED = "file processed"