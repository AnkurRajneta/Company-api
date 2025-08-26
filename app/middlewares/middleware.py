# app/middlewares/auth_middlewares.py
from fastapi import HTTPException, Request, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import get_db
from app.repository.user_repository import UserRepository
from app.utils.utils import decode_jwt

async def get_current_user(
    request: Request,
    db: AsyncSession = Depends(get_db)
):
    authorization = request.headers.get('Authorization')

    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid Authorization header"
        )

    # Extract token correctly (remove "Bearer ")
    token = authorization.split(" ")[1].strip()
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Empty token in Authorization header"
        )

    try:
        payload = decode_jwt(token)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid or expired token: {str(e)}"
        )

    user_id = payload.get("email")
    role_id = payload.get("role")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token missing subject (sub) claim"
        )

    try:
        user = await UserRepository(db).get_user_by_username_repository(user_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error while accessing user data"
        )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return {"user": user, "role_id": role_id}
