from fastapi import FastAPI, Depends
from fastapi.openapi.utils import get_openapi
from app.config.database import Base, engine
from app.models import *
from app.controller.role_controller import router as role_router
from app.controller.employee_controller import router as employee_router
from app.controller.user_controller import router as user_router
# from app.controller.auth_controller import router as auth_router
# from app.middlewares.auth_middleware import get_current_user

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = FastAPI(
    title="Office API",
    version="1.0.0"
)

# Routers
app.include_router(role_router, prefix="/api/v1/role", tags=["Role"])
app.include_router(employee_router, prefix="/api/v1/employee", tags=["Employee"])
app.include_router(user_router, prefix="/api/v1/user", tags=["User"])
# app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"]) 