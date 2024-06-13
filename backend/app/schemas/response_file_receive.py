from pydantic import BaseModel
from pydantic import Field

from .status import Status


class ResponseFileReceive(BaseModel):
    file: str = Field(..., title="File name sent by the frontend")
    file_renamed: str = Field(..., title="File renamed")
    status: Status = Field(..., title="Status file")
