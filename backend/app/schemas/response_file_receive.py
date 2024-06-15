from pydantic import BaseModel
from pydantic import Field


class ResponseFileReceive(BaseModel):
    file: str = Field(..., title="File name sent by the frontend")
    file_renamed: str = Field(..., title="File renamed")
    status: str = Field(..., title="Status file")
