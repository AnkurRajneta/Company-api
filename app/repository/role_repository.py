from app.models.role_models import RoleModel
from app.schema.role_schema import GetRoleSchema,CreateRoleSchema,UpdateRoleSchema
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from sqlalchemy import select

class RoleRepository:
    def __init__(self, db: AsyncSession):
          self.db = db

    async def create_roles_repository(self,payload:CreateRoleSchema):
         new_role = RoleModel(role = payload.role)
         self.db.add(new_role)
         await self.db.commit()
         await self.db.refresh(new_role)
         return new_role
    
    async def get_all_roles_repository(self):
         stmt = select(RoleModel)
         result = await self.db.execute(stmt)
         return  result.scalars().all()
    
    async def get_role_by_id_repository(self, id:int):
         stmt = select(RoleModel).where(RoleModel.id ==id)
         result = await self.db.execute(stmt)
         return  result.scalars().first()
    
    async def update_role_by_id_repository(self, id:int, payload:UpdateRoleSchema):
         stmt = select(RoleModel).where(RoleModel.id == id)
         result = await self.db.execute(stmt)
         updated_result = result.scalars().first()

         if not updated_result:
            raise HTTPException(status_code=404, detail="Role not found")
        

         updated_result.role = payload.role
         await self.db.commit()
         await self.db.refresh(updated_result)
         return updated_result
    

    async def delete_role_by_id_repository(self, id:int):
         stmt = select(RoleModel).where(RoleModel.id == id)
         result = await self.db.execute(stmt)
         deleted_item = result.scalars().first()

         if not deleted_item:
            raise HTTPException(status_code=404, detail="Role not found")
        
         await self.db.delete(deleted_item)
         await self.db.commit()
         return {"message": "Deleted successfully"}





    

