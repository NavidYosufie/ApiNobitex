from pydantic import BaseModel
from typing import Optional, Dict, Any


class InputSchema(BaseModel):
    payload: Optional[dict] = None


class OutputSchema(BaseModel):
    message: str
    data: Dict[str, Any]
