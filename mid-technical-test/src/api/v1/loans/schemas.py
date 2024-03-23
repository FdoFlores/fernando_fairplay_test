from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, constr, condecimal

class LoanSchema(BaseModel):
    amount: condecimal(max_digits = 21, decimal_places = 2)

class ReturnLoanSchema(LoanSchema):
    customer_id: UUID
    id: UUID
    created: datetime
    modified: datetime