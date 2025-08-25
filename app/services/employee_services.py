from app.repository.employee_repository import EmployeeRepository
from app.schema.employee_schema import *
from sqlalchemy.ext.asyncio import AsyncSession


class EmployeeServices:
    def __init__(self, db:AsyncSession):
        self.repo = EmployeeRepository(db)

    async def create_employee_service(self, payload:CreateEmployeeSchema):
        return await self.repo.create_employee_repository(payload)
    
    async def get_all_employee_service(self):
        return await self.repo.get_all_employee_repository()
    
    async def get_employee_by_id_service(self, id:int):
        return await self.repo.get_employee_id_repository(id)
    
    async def update_employee_by_id(self,id:int, payload:UpdateEmployeeSchema):
        return await self.repo.update_employee_id_repository(id, payload)
    
    async def delete_employee_by_id(self, id:int):
        return await self.repo.delete_employee_by_id(id)
