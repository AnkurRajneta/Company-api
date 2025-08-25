from app.models.employees_models import EmployeeModel
from app.models.user_models import UserModel
from sqlalchemy import select
from app.schema.employee_schema import *
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.enums.enums import *
from typing import List
from sqlalchemy.orm import selectinload


class EmployeeRepository:
    def __init__(self, db:AsyncSession):
        self.db = db

    async def create_employee_repository(self, payload:CreateEmployeeSchema):
        new_employee = EmployeeModel(name = payload.name,
                                     contact_no = payload.contact_no,
                                     status = payload.status,
                                     user_id = payload.user_id)
        
        self.db.add(new_employee)
        await self.db.commit()
        await self.db.refresh(new_employee)
        return new_employee
    
    async def get_all_employee_repository(self):
        stmt = select(EmployeeModel).options(selectinload(EmployeeModel.user).selectinload(UserModel.role))
        result = await self.db.execute(stmt)
        return result.scalars().all()
    

    async def get_employee_id_repository(self, id:int):
        stmt = select(EmployeeModel).where(EmployeeModel.id ==id).options(selectinload(EmployeeModel.user).selectinload(UserModel.role))
        result = await self.db.execute(stmt)
        return result.scalars().first()
    

    async def update_employee_id_repository(self,id:int,  payload:UpdateEmployeeSchema):
        stmt = select(EmployeeModel).where(EmployeeModel.id == id)
        result = await self.db.execute(stmt)
        updated_result = result.scalars().first()

        if not updated_result:
            raise HTTPException(status_code=404, detail="Employee not found")
        
        updated_result.name = payload.name
        updated_result.contact_no = payload.contact_no
        updated_result.status = payload.status
        updated_result._user_id = payload.user_id

        await self.db.commit()
        await self.db.refresh(updated_result)
        return updated_result
    

    async def delete_employee_by_id(self, id:int):
        stmt = select(EmployeeModel).where(EmployeeModel.id == id)
        result = await self.db.execute(stmt)
        deleted_item = result.scalars().first()

        if not deleted_item:
            raise HTTPException(status_code=404, detail="Book not found")

        await self.db.delete(deleted_item)
        await self.db.commit()
        return {"message": "Deleted successfully"}



        

