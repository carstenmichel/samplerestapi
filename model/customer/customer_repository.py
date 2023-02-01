from typing import List

from model.customer.customer import Customer

customers = [
    Customer(
        id=0,
        fname="Carsten",
        lname="Michel",
        city="Methler",
        email="noone@home.net"
    )
]


class CustomerRepository:
    def __init__(self):
        self._customers = customers

    def delete(self, customer_id: int):
        customer = next((q for q in self._customers if q.id == customer_id), None)
        if customer is not None:
            idx = self._customers.index(customer)
            self._customers.pop(idx)

    def get(self, customer_id: int) -> Customer:
        customer = next((q for q in self._customers if q.id == customer_id), None)
        return customer

    def add(self, customer: Customer) -> Customer:
        ids = [customer.id for customer in self._customers]
        customer.id = max(ids) + 1
        self._customers.append(customer)
        return customer

    def total_count(self) -> int:
        return len(self._customers)

    def query(self) -> List[Customer]:
        return self._customers

    def search(self, fname: str = "", lname: str = "") -> List[Customer]:
        duplicate = next((q for q in self._customers if q.fname == fname), None)
        return [duplicate] if duplicate is not None else []

    def update(self, fname: str, lname: str, customer_id: int) -> Customer:
        customer = next((q for q in self._customers if q.id == customer_id), None)
        if customer is not None:
            customer.fname = fname
            customer.lname = lname

        return customer
