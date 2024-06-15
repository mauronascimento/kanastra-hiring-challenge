from typing import List

from fastapi import HTTPException
from fastapi_sqlalchemy import db

from app.models.models import StatusFile
from app.models.models import Charges


class ChargeRepository:
    def save(self, list_charges: List[Charges]):
        try:
            db.session.bulk_save_objects(list_charges)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise HTTPException(status_code=400, detail=str(e))
