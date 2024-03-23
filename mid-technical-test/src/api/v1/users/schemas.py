from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    password: str
