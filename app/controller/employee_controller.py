from app.services.employee_services import EmployeeServices
from fastapi import APIRouter, Depends, HTTPException, status
from app.schema.employee_schema import *
from app.config.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.middlewares.middleware import get_current_user
from app.models.user_models import UserModel
from app.enums.enums import UserRoleEnum
from app.middlewares.response import StandardResponse

router = APIRouter()

@router.post("")
async def create_employee_controller(payload:CreateEmployeeSchema, db:AssertionError = Depends(get_db),current_user = Depends(get_current_user)):
    
    if current_user['role_id'] != UserRoleEnum.EMPLOYEES:
        
        service = EmployeeServices(db)
        result = await service.create_employee_service(payload)
        return {
            
            "data":result,
            "message":"Employee successfully created"
        }
    else:
        
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized User")
        

       

@router.get("",response_model = StandardResponse[List[EmployeeUserSchema]])
async def get_all_employee_controller(db:AsyncSession = Depends(get_db)):
    service = EmployeeServices(db)
    result = await service.get_all_employee_service()
    return {
        "data":result,
        "message":"All employees detail"
    }


@router.get("/id/{id}",response_model=StandardResponse[EmployeeUserSchema])
async def get_employee_by_id(id:int, db:AsyncSession = Depends(get_db)):
    service = EmployeeServices(db)
    result = await service.get_employee_by_id_service(id)
    return {
        "data":result,
        "message":"Getting Employee with particular id"
    }

@router.put("/update/{id}")
async def update_employees_by_id(payload:UpdateEmployeeSchema, id:int, db:AsyncSession = Depends(get_db),current_user = Depends(get_current_user)):
    if current_user['role_id'] != UserRoleEnum.EMPLOYEES:
        service = EmployeeServices(db)
        result = await service.update_employee_by_id(id, payload)
        return {
            "data":result,
            "message":"Updating the employee at particular id"
        }
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized User")

@router.delete("/delete/{id}")
async def delete_user_by_id_controller(id:int, db:AsyncSession = Depends(get_db),current_user = Depends(get_current_user)):
    if current_user['role_id'] != UserRoleEnum.EMPLOYEES:
        service = EmployeeServices(db)
        result = await service.delete_employee_by_id(id)
        return {
            "data":result,
            "message":"Removing the employee with specific id"
        }
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized User")
