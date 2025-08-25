
from app.services.user_services import UserService
from fastapi import APIRouter, Depends, HTTPException, status
from app.schema.user_schema import *
from app.config.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List


router = APIRouter()




@router.post("")
async def create_user_controller(payload:CreateUserSchema, db:AsyncSession = Depends(get_db)):
    service = UserService(db)
    result =  await service.create_user_service(payload)
    return result

@router.get("", response_model=List[GetUserSchema])
async def get_all_user_controller(db:AsyncSession = Depends(get_db)):
    service = UserService(db)
    result =  await service.get_all_user_service()
    return result

@router.get("/{id}",response_model=GetUserSchema)
async def get_user_by_id_controller(id:int, db:AsyncSession = Depends(get_db)):
    service = UserService(db)
    result = await service.get_user_by_id_service(id)
    return result

@router.put("/update/{id}")
async def update_user_by_id_controller(id:int, payload:UpdateUserSchema, db:AsyncSession = Depends(get_db)):
    service = UserService(db)
    result =  await service.update_user_by_id_service(id, payload)
    return result

@router.delete("/delete/{id}")
async def delete_user_by_id_controller(id:int, db:AsyncSession = Depends(get_db)):
    service = UserService(db)
    result = await service.delete_user_by_id_service(id)
    return result

