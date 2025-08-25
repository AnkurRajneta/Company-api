from sqlalchemy import Column, Integer, String, Boolean, Enum
from app.config.database import Base
from sqlalchemy.orm import relationship
from app.enums.enums import TableName, UserRoleEnum

class RoleModel(Base):
    __tablename__ = TableName.ROLE

    id = Column(Integer, primary_key= True)
    role = Column(Enum(UserRoleEnum), nullable= False)

    user = relationship("UserModel", back_populates="role")