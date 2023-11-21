from fastapi import APIRouter, Request, status, HTTPException, Depends
from src.api.schemas import request
from src.api.schemas import response
from typing import Annotated
from src.api.repository import EmployeeRepository


router = APIRouter(
    prefix="/employee",
    tags=["employee"],
)


@router.get(path="/{employee_id}", status_code=status.HTTP_200_OK)
async def get_employee_by_id(request: Request, employee_id: int) -> response.Employee:
    repository = EmployeeRepository(request.app.pool)
    result = await repository.get_employee(employee_id)
    if result:
        return response.Employee(age=result.get("age"), name=result.get("name"))
    
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f"employee not found", headers={"X-Error": "employee not found"})