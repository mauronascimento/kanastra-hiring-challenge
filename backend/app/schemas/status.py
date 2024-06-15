from enum import Enum


class Status(str):
    QUEUE = "queued to be processed"
    PROCESSIG = "file processing"
    PROCESSED = "file processed"
