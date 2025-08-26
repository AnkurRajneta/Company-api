from app.services.role_services import RoleService
from fastapi import APIRouter, Depends, HTTPException, status
from app.schema.role_schema import *
from app.config.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.middlewares.middleware import get_current_user
from app.middlewares.response import StandardResponse


router = APIRouter()


@router.post("")
async def create_role_controller(payload:CreateRoleSchema,db: AsyncSession = Depends(get_db),current_user = Depends(get_current_user)):
    if current_user['role_id'] == UserRoleEnum.ADMIN:
        service = RoleService(db)
        result = await service.create_role_services(payload)
        return {
            "data":result,
            "message":"Creating a particular role"
        }
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized User")
        

@router.get("", response_model=StandardResponse[List[GetRoleSchema]])
async def get_all_role_controller(db:AsyncSession = Depends(get_db)):
    service = RoleService(db)
    result = await service.get_all_role_services()
    return {
        "data":result,
        "message":"Getting all role in an organization"
    }

@router.get("/id/{id}", response_model=StandardResponse[GetRoleSchema])
async def get_role_by_id_controler(id:int, db:AsyncSession = Depends(get_db)):
    service = RoleService(db)
    result = await service.get_role_by_id(id)
    return {
        "data":result,
        "message":"Getting a particular role by id"
    }

@router.put("")
async def update_role_by_id_controller(id:int,payload:UpdateRoleSchema, db:AsyncSession = Depends(get_db),current_user = Depends(get_current_user)):
    if current_user['role_id'] ==UserRoleEnum.ADMIN:
        service = RoleService(db)
        result = await service.update_role_by_id(id, payload)
        return {
            "data":result,
            "message":"Updating particular role by id"
        }
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access")

@router.delete("/delete/{id}")
async def delete_role_by_id_controller(id:int,db:AsyncSession = Depends(get_db),current_user = Depends(get_current_user)):
    if current_user['role_id'] ==UserRoleEnum.ADMIN:
        service = RoleService(db)
        result = await service.delete_role_by_id(id)
        return {
            "data":result,
            "message":"Role with particular id is deleted successfully"
        }
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unautorized User")

