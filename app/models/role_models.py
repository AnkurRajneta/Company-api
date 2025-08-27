from sqlalchemy import Column, Integer, Enum
from app.config.database import Base
from sqlalchemy.orm import relationship
from app.enums.enums import TableName, UserRoleEnum

class RoleModel(Base):
    __tablename__ = TableName.ROLE

    id = Column(Integer, primary_key=True)
    role = Column(Enum(UserRoleEnum), nullable=False)

    user = relationship("UserModel", back_populates="role")

    role_permission_assocs = relationship("RolePermissionAssociation", back_populates="role")
    permissions = relationship(
        "PermissionModel",
        secondary="rolepermissionassociation",
        viewonly=True,
        back_populates="roles"
    )

    user_role_assocs = relationship("UserRoleAssociation", back_populates="role")  # <-- ADD THIS LINE