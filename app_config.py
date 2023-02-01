from enum import Enum

from lagom import Container, Singleton
from lagom.environment import Env
from lagom.integrations.fast_api import FastApiIntegration


from model.customer.customer_repository import CustomerRepository
from model.customer.customer_service import CustomerService

class DatabaseScheme(str, Enum):
    SQL = "sql",
    IN_MEMORY = "in_memory"


class AppConfig(Env):
    database_scheme: DatabaseScheme = DatabaseScheme.IN_MEMORY


container = Container(log_undefined_deps=True)

container[CustomerRepository] = Singleton(CustomerRepository)
container[CustomerService] = Singleton(CustomerService)

deps = FastApiIntegration(container)
