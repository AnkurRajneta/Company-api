from datetime import timedelta
from fastapi import HTTPException, status
from app.repository.user_repository import UserRepository
from app.repository.role_repository import RoleRepository
from app.schema.auth_schema import *
from sqlalchemy.ext.asyncio import AsyncSession
from app.utils import utils
from app.enums.enums import UserRoleEnum,Permissions

# Role to permissions mapping
ROLE_PERMISSIONS = {
    UserRoleEnum.ADMIN.value: [
         Permissions.CREATE_EMPLOYEE_CONTROLLER.value,
        Permissions.UPDATE_EMPLOYEES_BY_ID.value,
        Permissions.DELETE_USER_BY_ID_CONTROLLER.value,
        Permissions.CREATE_ROLE_CONTROLLER.value,
        Permissions.UPDATE_ROLE_BY_ID_CONTROLLER.value,
        Permissions.DELETE_ROLE_BY_ID_CONTROLLER.value,
    ],
    UserRoleEnum.HR.value: [
        Permissions.CREATE_EMPLOYEE_CONTROLLER.value,
        Permissions.UPDATE_EMPLOYEES_BY_ID.value,
        Permissions.DELETE_USER_BY_ID_CONTROLLER.value,
    ],
    UserRoleEnum.EMPLOYEES.value: [
        # Employees can only view, so no write permissions
    ]
}

class AuthService:
    def __init__(self, db: AsyncSession):
        self.repo = UserRepository(db)

    async def auth_service(self, email: EmailStr, password: str):
        if not email or not password:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Please provide email and password"
            )
        user = await self.repo.get_user_by_username_repository(email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        if not password == user.password:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="Password is incorrect"
            )

        # Dynamically assign permissions based on role
        user_role = user.role.role if hasattr(user.role, 'role') else user.role
        permissions = ROLE_PERMISSIONS.get(user_role, [])

        token_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            "role_id": user.role_id,
            "role": user_role,
            "permissions": permissions
        }

        token = utils.create_jwt(data=token_data, expires_delta=timedelta(30))

        return {
            "status_code": 200,
            "error": None,
            "message": "Logged in successfully",
            "data": {
                "access_token": token,
                "user": {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    "role_id": user.role_id,
                    "role": user_role,
                    "permissions": permissions
                }
            }
        }

    async def register_auth(self, payload: RegisterSchema):
        new_user = await self.repo.create_user_repository(payload)
        return new_user