

from typing import Any, Dict
from fastapi import UploadFile, File
# from fastapi import HTTPException
# from sqlalchemy.orm import Session
# from app.schemas.schemas import Charges
# from app.models.models import ChargesModel
from backend.app.schemas.response_file_receive import ResponseFileReceive

class ProcessesReceivedFile:

    @staticmethod
    def received_save(teste):
        pass
        #
        # file_name = teste.filename
        # generate_name_timestamp = str(datetime.timestamp(datetime.now())).replace(".", "")
        # file_renamed = f"{generate_name_timestamp}-{file_name}"
        # path = f"app/files/{file_renamed}"
        # with open(path, 'w+b') as file:
        #     shutil.copyfileobj(uploaded_file.file, file)
        #
        # return ResponseFileReceive(
        #     file= uploaded_file.filename,
        #     file_renamed=file_renamed,
        #     status=Status.QUEUE,
        # )
