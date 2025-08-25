from app.services.employee_services import EmployeeServices
from fastapi import APIRouter, Depends, HTTPException, status
from app.schema.employee_schema import *
from app.config.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List


router = APIRouter()

@router.post("")
async def create_employee_controller(payload:CreateEmployeeSchema, db:AssertionError = Depends(get_db)):
    service = EmployeeServices(db)
    result = await service.create_employee_service(payload)
    return result


@router.get("",response_model = List[GetEmployeeSchema])
async def get_all_employee_controller(db:AsyncSession = Depends(get_db)):
    service = EmployeeServices(db)
    result = await service.get_all_employee_service()
    return result

@router.get("/id/{id}",response_model=GetEmployeeSchema)
async def get_employee_by_id(id:int, db:AsyncSession = Depends(get_db)):
    service = EmployeeServices(db)
    result = await service.get_employee_by_id_service(id)
    return result

@router.put("/update/{id}")
async def update_employees_by_id(payload:UpdateEmployeeSchema, id:int, db:AsyncSession = Depends(get_db)):
    service = EmployeeServices(db)
    result = await service.update_employee_by_id(id, payload)
    return result

@router.delete("/delete/{id}")
async def delete_user_by_id_controller(id:int, db:AsyncSession = Depends(get_db)):
    service = EmployeeServices(db)
    result = await service.delete_employee_by_id(id)
    return result
