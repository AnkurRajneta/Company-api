from pydantic import BaseModel
from typing import Optional
from app.enums.enums import UserRoleEnum
class CreateRoleSchema(BaseModel):
    role:UserRoleEnum
    
    class Config:
        from_attributes = True



class UpdateRoleSchema(BaseModel):
    role : Optional[UserRoleEnum] = None
    class Config:
        from_attributes = True


class GetRoleSchema(BaseModel):
    id:int
    role:UserRoleEnum

    class Config:
        from_attributes = True
    