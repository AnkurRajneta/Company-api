from app.repository.role_repository import *
from app.schema.role_schema import *
from sqlalchemy.ext.asyncio import AsyncSession


class RoleService:
    def __init__(self, db:AsyncSession):
        self.repo = RoleRepository(db)

    async def create_role_services(self, payload:CreateRoleSchema):
        return await self.repo.create_roles_repository(payload)
    
    async def get_all_role_services(self):
        return await self.repo.get_all_roles_repository()
    
    async def get_role_by_id(self, id:int):
        return await self.repo.get_role_by_id_repository(id)
    
    async def update_role_by_id(self, id:int, payload:UpdateRoleSchema):
        return await self.repo.update_role_by_id_repository(id, payload)
    
    async def delete_role_by_id(self, id:int):
        return await self.repo.delete_role_by_id_repository(id)