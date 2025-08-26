from datetime import timedelta
from fastapi import HTTPException,status
from app.repository.user_repository import UserRepository
from app.repository.role_repository import RoleRepository
from app.schema.auth_schema import *
from sqlalchemy.ext.asyncio import AsyncSession
from app.utils import utils


class AuthService:
    def __init__(self, db:AsyncSession):
        self.repo = UserRepository(db)

    async def auth_service(self, email:EmailStr, password:str):
        if not email or not password:
            return HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                message = "Please provide email and password"
            )
        user = await self.repo.get_user_by_username_repository(email)
        
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                message="User not found"
            )
        
        
        if not password==user.password:
            return HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                message="Password is incorrect"
            )
        token_data = {
            'id':user.id,
            'username':user.username,
            'email':user.email,
            "role_id":user.role_id,
            "role":user.role.role
            
        }

        token = utils.create_jwt(data=token_data, expires_delta=timedelta(30))
        
        return {
            
            "status_code":200,
            "error":None,
            "message":"Logged in successfully",
            "data":{
                "access_token":token,
                 "user":{
                     'id':user.id,
                    'username':user.username,
                    'email':user.email,
                    "role_id":user.role_id,
                    "role":user.role.role
                     
                 }
            }
        }
    

    async def register_auth(self, payload:RegisterSchema):
        new_user = await self.repo.create_user_repository(payload)
        return new_user