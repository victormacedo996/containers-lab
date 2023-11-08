from fastapi import APIRouter, Request, status, HTTPException, Depends
from src.api.schemas import request
from src.api.schemas import response
from typing import Annotated
from src.api.repository import EmployeeRepository


router = APIRouter(
    prefix="/employee",
    tags=["employee"],
)


@router.get(path="/", status_code=status.HTTP_200_OK)
async def get_employee_by_id(request: Request, data: request.GetEmployeeById) -> response.Employee:
    repository = EmployeeRepository(request.app.pool)
    result = await repository.get_employee(data.employee_id)
    if result:
        return response.Employee(age=result.get("age"), name=result.get("name"))
    
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f"employee not found")