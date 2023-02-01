from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel
from model.customer.customer import Customer

class AddCustomerRequest(BaseModel):
    fname: str
    lname: str
    city: Optional[str] = ""
    email: Optional[str] = ""


class UpdateCustomerRequest(BaseModel):
    id: int
    fname: str
    lname: str
    city: Optional[str] = ""
    email: Optional[str] = ""


class CustomersResponse(BaseModel):
    customers: List[Customer]
    totalCount: int


class CustomerResponse(BaseModel):
    customer: Customer


class AddCustomerResponse(BaseModel):
    customer: Customer
    date_added: datetime
