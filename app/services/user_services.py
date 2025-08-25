from app.repository.user_repository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from app.schema.user_schema import *

# from app.enums.enums import UserRoleEnum as Enum
# from sqlalchemy import select
# from app.models.user_model import UserModel


class UserService:
    def __init__(self, db:AsyncSession):
        self.repo = UserRepository(db)

       
    async def create_user_service(self, payload:CreateUserSchema):
        return await self.repo.create_user_repository(payload)
    
    async def get_user_by_username_service(self,username:str):
        return await self.repo.get_user_by_username_repository(username)
    
    async def get_all_user_service(self):
        return await self.repo.get_all_user_repository()
    
    async def get_user_by_id_service(self,id:int):
        return await self.repo.get_user_by_id_repository(id)
    
    async def update_user_by_id_service(self,id:int, payload:UpdateUserSchema):
        return await self.repo.update_user_by_id_repository(id, payload)
    
    async def delete_user_by_id_service(self, id:int):
        return await self.repo.delete_user_by_id_repository(id)
    

    