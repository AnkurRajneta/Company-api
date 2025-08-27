from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
from app.enums.enums import TableName


class RolePermissionAssociation(Base):
    __tablename__ = TableName.ROLEPERMISSIONASSOCIATION

    role_id = Column(Integer, ForeignKey("role.id"), primary_key=True)
    permission_id = Column(Integer, ForeignKey("permissions.id"), primary_key=True)

    

    role = relationship("RoleModel", back_populates="role_permission_assocs")
    permission = relationship("PermissionModel", back_populates="role_permission_assocs")


class UserRoleAssociation(Base):
    __tablename__ = "user_role_association"
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    role_id = Column(Integer, ForeignKey("role.id"), primary_key=True)

    user = relationship("UserModel", back_populates="user_role_assocs")
    role = relationship("RoleModel", back_populates="user_role_assocs")
