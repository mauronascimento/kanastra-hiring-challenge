import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, Date, Index, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from app.schemas.response_file_receive import ResponseFileReceive

Base = declarative_base()


class Charges(Base):
    __tablename__ = "charges"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    government_id = Column(String)
    email = Column(String)
    debt_amount = Column(Float)
    debt_due_date = Column(Date)
    is_send_email = Column(Boolean, unique=False, default=False)
    is_send_ticket = Column(Boolean, unique=False, default=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now)

    __table_args__ = (Index("idx_charges_id", "id"),)


class StatusFile(Base):
    __tablename__ = "status_file"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_file = Column(String)
    file_renamed = Column(String)
    status = Column(String)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now)

    __table_args__ = (Index("idx_status_file", "id"),)

    def __init__(self, response_file_receive: ResponseFileReceive):
        self.name_file = response_file_receive.file
        self.file_renamed = response_file_receive.file_renamed
        self.status = response_file_receive.status
