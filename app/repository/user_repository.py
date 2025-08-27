from app.models.user_models import UserModel
from sqlalchemy import select
from app.schema.user_schema import *
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.enums.enums import *
from typing import List
from sqlalchemy.orm import selectinload
class UserRepository:
    def __init__(self, db:AsyncSession):
        self.db = db

    async def create_user_repository(self, payload:CreateUserSchema):
        new_user = UserModel(username = payload.username,
                             email = payload.email,
                             password = payload.password,
                             role_id = payload.role_id)
        
        self.db.add(new_user)
        await self.db.commit()
        self.db.refresh(new_user)
        return new_user
    

    async def get_user_by_username_repository(self,email:EmailStr):
        user = select(UserModel).where(UserModel.email ==email).options(selectinload(UserModel.role),selectinload(UserModel.employees))
        result = await self.db.execute(user)
        return result.scalars().first()

    async def get_all_user_repository(self):
        stmt = select(UserModel).options(selectinload(UserModel.role),selectinload(UserModel.employees))
        result = await self.db.execute(stmt)
        return result.scalars().all()
    
    async def get_user_by_id_repository(self, id:int):
        stmt = select(UserModel).where(UserModel.id == id).options(selectinload(UserModel.role),selectinload(UserModel.employees))
        result = await self.db.execute(stmt)
        return result.scalars().first()
    
    async def update_user_by_id_repository(self,id: int, payload:UpdateUserSchema):
        stmt = select(UserModel).where(UserModel.id == id)
        result = await self.db.execute(stmt)
        updated_result =  result.scalars().first()

        if not updated_result:
            raise HTTPException(status_code=404, detail="User Not Found")
        
        updated_result.username = payload.username
        updated_result.email = payload.email
        updated_result.password = payload.password
        updated_result.role_id = payload.role_id

        await self.db.commit()
        await self.db.refresh(updated_result)
        return updated_result
    
    async def delete_user_by_id_repository(self, id: int):
        stmt = select(UserModel).where(UserModel.id == id)
        result = await self.db.execute(stmt)
        deleted_item = result.scalars().first()

        if not deleted_item:
            raise HTTPException(status_code=404, detail="User not found")
        
        await self.db.delete(deleted_item)
        await self.db.commit()
        return {"message": "Deleted successfully"}
     
        



