import uuid

from sqlalchemy import Column, Integer, String, Float, Date, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class Charges(Base):
    __tablename__ = 'charges'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    government_id = Column(String)
    email = Column(String)
    debt_amount = Column(Float)
    debt_due_date = Column(Date)

    __table_args__ = (Index('idx_charges_id', 'id'),)



class StatusFile(Base):
    __tablename__ = 'status_file'
    id =  Column(Integer, primary_key=True, autoincrement=True)
    name_file = Column(String)
    file_renamed = Column(String)
    status = Column(String)
    create_at = Column(Date)

    __table_args__ = (Index('idx_status_file', 'id'),)