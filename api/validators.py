from typing import Optional

from pydantic import BaseModel


class Item(BaseModel):
    alphabet: Optional[int] = 0
    real_numbers: Optional[int] = 0
    integers: Optional[int] = 0
    alphanumeric: Optional[int] = 0
