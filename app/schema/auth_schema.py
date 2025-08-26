from pydantic import BaseModel,EmailStr
from typing import Optional
from app.enums.enums import UserRoleEnum


class AuthSchema(BaseModel):
    email:EmailStr
    password:str
    class Config:
        from_attributes = True

class RegisterSchema(BaseModel):
    username:Optional[str]
    email:Optional[EmailStr]
    password:Optional[str]
    role_id: int  
    class Config:
        from_attributes = True

class RegisterOut(BaseModel):
    id:int
    username:str
    email:EmailStr

    class Config:
        from_attributes = True