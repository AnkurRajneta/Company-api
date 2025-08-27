from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship
from app.enums.enums import TableName


class UserModel(Base):
      __tablename__ = TableName.USER
      
      id = Column(Integer, primary_key=True)
      username = Column(String,nullable= False)
      email = Column(String, nullable= False)
      password = Column(String, nullable= False)
      role_id = Column(Integer, ForeignKey("role.id"))


      role = relationship("RoleModel", back_populates="user")

      employees = relationship("EmployeeModel", back_populates="user")
     
    
