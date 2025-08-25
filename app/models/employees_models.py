from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
from app.enums.enums import TableName, ActiveEnum

class EmployeeModel(Base):
    __tablename__ = TableName.EMPLOYEES

    id = Column(Integer, primary_key= True)
    name = Column(String, nullable= False)
    contact_no = Column(Integer, nullable= False)
    status = Column(Enum(ActiveEnum), nullable= False)
    user_id = Column(Integer,ForeignKey("user.id"))


    user = relationship("UserModel", back_populates="employees")

    