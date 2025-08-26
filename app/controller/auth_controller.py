from fastapi import HTTPException, APIRouter, status, Depends
from fastapi import security
from sqlalchemy.ext.asyncio import AsyncSession
from app.schema.auth_schema import *

from app.config.database import get_db
from app.services.auth_services import AuthService
from app.middlewares.middleware import get_current_user
from fastapi.security import HTTPBearer
from app.middlewares.response import StandardResponse



router = APIRouter()

security = HTTPBearer()


@router.post('/login')
async def login(payload:AuthSchema, db: AsyncSession = Depends(get_db)):
    service = AuthService(db)
    user = await service.auth_service(payload.email, payload.password)    
    return {
        "value": user,
        "message": "Token Generated Successfully"
    }
    

@router.post('/register', response_model=StandardResponse[RegisterOut])
async def register(payload:RegisterSchema, db: AsyncSession = Depends(get_db)):
    service = AuthService(db)
    result =  await service.register_auth(payload)
    return {
        
        "data":result,
        "message":"User Registered Successfully"
    }

@router.get('/me')
def me(current_user = Depends(get_current_user)):
    return current_user