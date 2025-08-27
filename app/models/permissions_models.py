from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
from app.enums.enums import TableName

class PermissionModel(Base):
    __tablename__ = TableName.PERMISSIONS

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    role_id = Column(Integer, ForeignKey("role.id"))

    
    role = relationship(
        "RoleModel",
        back_populates="permissions",
    )