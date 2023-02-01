from typing import Optional

from pydantic import BaseModel


class Customer(BaseModel):
    id: Optional[int]
    fname: str
    lname: str
    city: Optional[str] = ""
    email: Optional[str] = ""

    