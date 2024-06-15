import csv
import uuid

from fastapi import HTTPException
from app.schemas.response_file_receive import ResponseFileReceive
from app.repositories.status_file_repository import StatusFileRepository
from app.repositories.charges_repository import ChargeRepository
from app.models.models import StatusFile
from app.models.models import ChargesModel
from app.schemas.status import Status
from app.schemas.charges import Charges
from app.commons.paginate import paginate


class ProcessesReceivedFile:
    @staticmethod
    def received_save(data_file: ResponseFileReceive):
        try:
            return StatusFileRepository().saves_files(StatusFile(data_file))
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def processes_file(path: str):
        try:
            list_charges = []
            with open(path, "r") as file:
                file_csv = csv.reader(file, delimiter=",")
                for i, line in enumerate(file_csv):
                    if i != 0:
                        list_charges.append(
                            ChargesModel(
                                Charges(
                                    name=line[0],
                                    government_id=line[1],
                                    email=line[2],
                                    debt_amount=float(line[3]),
                                    debt_due_date=line[4],
                                    debt_id=line[5],
                                )
                            )
                        )
                ChargeRepository().save(list_charges)
        except Exception as e:
            print(str(e))
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
