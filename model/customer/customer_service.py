from lagom.environment import Env

from model.customer.customer import Customer
from model.customer.customer_repository import CustomerRepository


class CustomerConfig(Env):
    ensure_unique_text: bool = False


class CustomerService:

    def __init__(self, customer_repository: CustomerRepository, config: CustomerConfig):
        self._customer_repository = customer_repository
        self._config = config

    async def add_customer(self, fname, lname) -> Customer:
        customer = Customer(fname=fname, lname=lname)

        customer_added = self._customer_repository.add(customer)
        return customer_added
