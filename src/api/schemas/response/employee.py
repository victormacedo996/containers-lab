from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    age: int