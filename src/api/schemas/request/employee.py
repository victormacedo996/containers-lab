from pydantic import BaseModel


class GetEmployeeById(BaseModel):
    employee_id: int