from fastapi import FastAPI, Depends
from fastapi.openapi.utils import get_openapi
from app.config.database import Base, engine
from app.models import *
from app.controller.role_controller import router as role_router
from app.controller.employee_controller import router as employee_router
from app.controller.user_controller import router as user_router
from app.controller.auth_controller import router as auth_router
from app.middlewares.response import CreateResponseMiddleware
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



app = FastAPI(
    title="Office API",
    version="1.0.0"
)


app.add_middleware(CreateResponseMiddleware)

# Routers
app.include_router(role_router, prefix="/api/v1/role", tags=["Role"])
app.include_router(employee_router, prefix="/api/v1/employee", tags=["Employee"])
app.include_router(user_router, prefix="/api/v1/user", tags=["User"])
app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"]) 




@app.get("/")
def root():
    return {"message": "Welcome to Book API"}  # fixed typo: Blog API -> Book API

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        routes=app.routes,
    )

    # Define Bearer token auth scheme
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }

    # Apply security globally
    openapi_schema["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
