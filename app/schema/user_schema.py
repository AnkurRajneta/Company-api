from pydantic import BaseModel, EmailStr
from typing import Optional, List
from app.schema.role_schema import GetRoleSchema
from app.schema.employee_schema import EmployeeUserSchema

class CreateUserSchema(BaseModel):
    username:str
    email: EmailStr
    password:str
    role_id:int

    class Config:
        from_attributes = True

class UpdateUserSchema(BaseModel):
    username : Optional[str] = None
    email : Optional[EmailStr] = None
    password : Optional[str] = None
    role_id : Optional[int]  = None
    
    class Config:
        from_attributes = True


class EmployeeGetUserSchema(BaseModel):
    id:int
    username:str
    email: EmailStr
    role_id:int

    class Config:
        from_attributes = True
class GetUserSchema(BaseModel):
    id:int
    username:str
    email: EmailStr
    password:str
    role_id:int
    role : Optional[GetRoleSchema] = None
    employees:Optional[List[EmployeeUserSchema]] = None

    class Config:
        from_attributes = True


    