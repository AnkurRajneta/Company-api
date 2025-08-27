from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.database import Base
from app.enums.enums import TableName

class PermissionModel(Base):
    __tablename__ = TableName.PERMISSIONS

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    role_permission_assocs = relationship("RolePermissionAssociation", back_populates="permission")
    roles = relationship(
        "RoleModel",
        secondary="rolepermissionassociation",  # <-- fixed: must match __tablename__ in RolePermissionAssociation
        viewonly=True,
        back_populates="permissions",
    )