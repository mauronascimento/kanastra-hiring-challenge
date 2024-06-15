
from typing import List

from fastapi import APIRouter, Request, UploadFile, File
from app.services.processes_received_file import ProcessesReceivedFile
from app.schemas.response_file_receive import ResponseFileReceive


router = APIRouter()


@router.get(
    "/list-status-file",
    response_model=List[ResponseFileReceive],
    summary="list-status-file",
    response_model_exclude_unset=True,
)
def list_status_file():
    list_response_file = []
    list_data_db = ProcessesReceivedFile.list_status_file()
    for data_db in list_data_db:
        list_response_file.append(
            ResponseFileReceive(
                file=data_db.name_file,
                file_renamed=data_db.file_renamed,
                status=data_db.status,
            )
        )

    return list_response_file
