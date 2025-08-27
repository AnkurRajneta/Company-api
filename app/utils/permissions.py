from fastapi import Depends, HTTPException, status
from app.enums.enums import Permissions
from app.middlewares.middleware import get_current_user

def require_permission(permission: Permissions):
    async def dependency(current_user = Depends(get_current_user)):
        # Assume current_user['permissions'] is a list of permission strings
        # If not, fetch permissions from DB based on user's role
        user_permissions = current_user.get('permissions', [])
        print(user_permissions)
        print("Checking permission:", permission.value, "in", user_permissions)
        if permission.value not in user_permissions:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action."
            )
    return dependency