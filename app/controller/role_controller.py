from app.services.role_services import RoleService
from fastapi import APIRouter, Depends, HTTPException, status
from app.schema.role_schema import *
from app.config.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List


router = APIRouter()


@router.post("", response_model=GetRoleSchema)
async def create_role_controller(payload:CreateRoleSchema,db: AsyncSession = Depends(get_db)):
    service = RoleService(db)
    result = await service.create_role_services(payload)
    return result

@router.get("", response_model=List[GetRoleSchema])
async def get_all_role_controller(db:AsyncSession = Depends(get_db)):
    service = RoleService(db)
    result = await service.get_all_role_services()
    return result

@router.get("/id/{id}", response_model=GetRoleSchema)
async def get_role_by_id_controler(id:int, db:AsyncSession = Depends(get_db)):
    service = RoleService(db)
    result = await service.get_role_by_id(id)
    return result

@router.put("")
async def update_role_by_id_controller(id:int,payload:UpdateRoleSchema, db:AsyncSession = Depends(get_db)):
    service = RoleService(db)
    result = await service.update_role_by_id(id, payload)
    return result

@router.delete("/delete/{id}")
async def delete_role_by_id_controller(id:int,db:AsyncSession = Depends(get_db)):
    service = RoleService(db)
    result = await service.delete_role_by_id(id)
    return result

