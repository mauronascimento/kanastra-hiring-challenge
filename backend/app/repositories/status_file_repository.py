from fastapi_sqlalchemy import db

from app.models.models import StatusFile


class StatusFileRepository:
    def saves_files(self, status_file: StatusFile):
        db.session.add(status_file)
        db.session.commit()
        return status_file.id

    def update_status_file(self, id: int, status: str):
        db.session.query(StatusFile).filter(StatusFile.id == id).update(
            {"status": status}
        )
        db.session.commit()

    def list_status_file(self):
        query = db.session.query(StatusFile).all()
        if query:
            return query
