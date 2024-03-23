from datetime import time
from typing import List, Optional

from ..loans.schemas import ReturnLoanSchema
from pydantic import BaseModel, constr

class CostumerSchema(BaseModel):
    full_name: constr(strict=True, max_length = 200)
    email: constr(strict=True, max_length = 200)

class ReturnCostumer(CostumerSchema):
    loans: Optional[List[ReturnLoanSchema]]