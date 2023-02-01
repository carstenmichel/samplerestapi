from datetime import datetime

from fastapi import APIRouter, Depends, status, HTTPException
from starlette.responses import Response



from app_config import deps
from model.customer.models import CustomersResponse,CustomerResponse, AddCustomerRequest, AddCustomerResponse, UpdateCustomerRequest
from model.customer.customer_repository import CustomerRepository
from model.customer.customer_service import CustomerService
import logging

router = APIRouter(
    prefix="/api/customer",
    tags=["customer"]
)


@router.get("", response_model=CustomersResponse, status_code=status.HTTP_200_OK)
async def query_customers(
        customer_repo: CustomerRepository = deps.depends(CustomerRepository)):
    total_count =  customer_repo.total_count()
    logging.warning("Got %d records", total_count)
    customers =  customer_repo.query()
    logging.warning("And received %s data", customers)
    return CustomersResponse(customers=customers, totalCount=total_count)


@router.get("/{customer_id}", response_model=CustomerResponse, status_code=status.HTTP_200_OK)
async def query_customer(
        customer_id: int,
        customer_repo: CustomerRepository = deps.depends(CustomerRepository)):
    customer = await customer_repo.get(customer_id)
    if customer is not None:
        return CustomerResponse(customer=customer)
    else:
        raise HTTPException(status_code=404)


@router.post("", response_model=AddCustomerResponse, status_code=status.HTTP_201_CREATED)
async def add_customer(
        add_customer_request: AddCustomerRequest,
        customer_service: CustomerService = deps.depends(CustomerService)):
        customer_added =  customer_service.add_customer(add_customer_request.fname, add_customer_request.lname)
        return AddCustomerResponse(customer=customer_added, date_added=datetime.now())


@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer(
        customer_id: int,
        customer_repo: CustomerRepository = deps.depends(CustomerRepository)):
    customer_repo.delete(customer_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{customer_id}", response_model=CustomerResponse, status_code=status.HTTP_200_OK)
async def update_customer(
        customer_id: int,
        update_customer_request: UpdateCustomerRequest,
        customer_repo: CustomerRepository = deps.depends(CustomerRepository)):
    updated_customer =  customer_repo.update(update_customer_request.fname, update_customer_request.lname, customer_id)
    if updated_customer is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    return CustomerResponse(customer=updated_customer)
