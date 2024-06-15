import logging
import time
import shutil
from datetime import datetime

from fastapi import APIRouter, Request, UploadFile, File
from app.services.processes_received_file import ProcessesReceivedFile
from app.schemas.status import Status
from app.schemas.response_file_receive import ResponseFileReceive


router = APIRouter()


@router.post(
    "/upload-file",
    response_model=ResponseFileReceive,
    summary="upload-file",
    response_model_exclude_unset=True,
    status_code=201,
)
def receive_upload_file(uploaded_file: UploadFile = File(...)):

    initial_time = time.time()
    file_name = uploaded_file.filename
    generate_name_timestamp = str(datetime.timestamp(datetime.now())).replace(".", "")
    file_renamed = f"{generate_name_timestamp}-{file_name}"
    path = f"app/files/{file_renamed}"
    with open(path, "w+b") as file:
        shutil.copyfileobj(uploaded_file.file, file)
    data_file = ResponseFileReceive(
        file=file_name, file_renamed=file_renamed, status=Status.QUEUE
    )
    id_file = ProcessesReceivedFile.received_save(data_file)
    ProcessesReceivedFile.processes_file(path)

    data_file.status = Status.PROCESSED
    ProcessesReceivedFile.update_status_file(id_file)

    final_time = time.time()
    print(f"runtime: {final_time - initial_time}")
    return data_file
