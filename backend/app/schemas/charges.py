from pydantic import BaseModel
from pydantic import Field


class Charges(BaseModel):
    debt_id: str = Field(..., title="Debt Id")
    name: str = Field(..., title="name")
    government_id: str = Field(..., title="Government Id")
    email: str = Field(..., title="email")
    debt_amount: float = Field(..., title="Debt Amount")
    debt_due_date: str = Field(..., title="Debt due date")
