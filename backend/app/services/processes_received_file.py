from fastapi import HTTPException
from app.schemas.response_file_receive import ResponseFileReceive
from app.repositories.status_file_repository import StatusFileRepository
from app.models.models import StatusFile
from app.schemas.status import Status


class ProcessesReceivedFile:
    @staticmethod
    def received_save(data_file: ResponseFileReceive):

        try:
            return StatusFileRepository().saves_files(StatusFile(data_file))
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def read_processes(data_file: ResponseFileReceive):

        try:
            StatusFileRepository().StatusFileRepository(data_file)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_status_file(id_file: int):
        try:
            return StatusFileRepository().update_status_file(id_file, Status.PROCESSED)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def list_status_file():
        try:
            return StatusFileRepository().list_status_file()
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
