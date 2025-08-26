
from app.services.user_services import UserService
from fastapi import APIRouter, Depends, HTTPException, status
from app.schema.user_schema import *
from app.config.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.middlewares.response import StandardResponse


router = APIRouter()




@router.post("")
async def create_user_controller(payload:CreateUserSchema, db:AsyncSession = Depends(get_db)):
    
        service = UserService(db)
        result =  await service.create_user_service(payload)
        return {
            "data":result,
            "message":"User is created successfully"
        }
   

@router.get("", response_model=StandardResponse[List[GetUserSchema]])
async def get_all_user_controller(db:AsyncSession = Depends(get_db)):
    service = UserService(db)
    result =  await service.get_all_user_service()
    return {
        "data":result,
        "message":"Getting all the users"
    }

@router.get("/{id}")
async def get_user_by_id_controller(id:int, db:AsyncSession = Depends(get_db)):
    service = UserService(db)
    result = await service.get_user_by_id_service(id)
    return {
        "data":result,
        "message":"Getting details with particular id"
    }

@router.put("/update/{id}")
async def update_user_by_id_controller(id:int, payload:UpdateUserSchema, db:AsyncSession = Depends(get_db)):
    service = UserService(db)
    result =  await service.update_user_by_id_service(id, payload)
    return {
        "data":result,
        "message":"Updating result with particular id"
    }

@router.delete("/delete/{id}")
async def delete_user_by_id_controller(id:int, db:AsyncSession = Depends(get_db)):
    service = UserService(db)
    result = await service.delete_user_by_id_service(id)
    return {
        "data":result,
        "message":"User with particular id is deleted successfully"
    }

