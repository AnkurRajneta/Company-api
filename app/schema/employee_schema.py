from pydantic import BaseModel
from typing import Optional 
from app.enums.enums import ActiveEnum
# from app.schema.user_schema import GetUserSchema

class CreateEmployeeSchema(BaseModel):
    name:str
    contact_no:int
    status:ActiveEnum
    user_id:int
    
    class Config:
        from_attributes = True

class UpdateEmployeeSchema(BaseModel):
    name: Optional[str] = None
    contact_no: Optional[int] = None
    status: Optional[ActiveEnum] = None
    user_id : Optional[int] = None

    class Config:
        from_attributes = True


class EmployeeUserSchema(BaseModel):
    id:int
    name: str
    contact_no:int
    user_id:int

    class Config:
        from_attributes = True


class GetEmployeeSchema(BaseModel):
    id:int
    name: str
    contact_no:int
    user_id:int

    class Config:
        from_attributes = True

