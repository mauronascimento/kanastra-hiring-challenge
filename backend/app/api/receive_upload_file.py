
import shutil
from datetime import datetime

from fastapi import APIRouter, Request, UploadFile, File

# from fastapi.responses import JSONResponse
# from starlette.responses import RedirectResponse
# from app.schemas.schemas import Charges
# from app.services.service import ChargeService
# from sqlalchemy.orm import Session
# from app.config.db import get_db
# from backend.app.services.processes_received_file import ProcessesReceivedFile
from app.schemas.status import Status
from app.schemas.response_file_receive import ResponseFileReceive


router = APIRouter()


@router.post(
    "/upload-file",
    response_model=ResponseFileReceive,
    summary="Proposta URL.",
    response_model_exclude_unset=True,
    status_code=201,
)
def receive_upload_file(uploaded_file: UploadFile = File(...)):
    file_name = uploaded_file.filename
    generate_name_timestamp = str(datetime.timestamp(datetime.now())).replace(".", "")
    file_renamed = f"{generate_name_timestamp}-{file_name}"
    path = f"app/files/{file_renamed}"
    with open(path, "w+b") as file:
        shutil.copyfileobj(uploaded_file.file, file)

    return ResponseFileReceive(
        file=file_name, file_renamed=file_renamed, status=Status.QUEUE
    )
