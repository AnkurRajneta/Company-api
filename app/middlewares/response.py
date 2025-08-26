from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import TypeVar, Generic, Optional
import json

T = TypeVar("T")

# Generic response wrapper model
class StandardResponse(GenericModel, Generic[T]):
    
    data: Optional[T]
    message: Optional[str]


class CreateResponseMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        try:
            body = [section async for section in response.body_iterator]
            raw_body = b"".join(body).decode()
            original_data = json.loads(raw_body)
        except Exception:
            original_data = {}

        message = original_data.pop("message", None)
        formatted_response = {
            "status": "success",
            "data": original_data,
            "message": message or "Failed Authorization"
        }
        return JSONResponse(content=formatted_response, status_code=response.status_code)