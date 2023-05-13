from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy import Column,Integer, String,ForeignKey
from .database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class Teacher(Base):
    __tablename__ = "Student_info"
    id = Column(Integer,nullable=False,primary_key=True,index=True,autoincrement=True)
    email=Column(String,nullable = False,unique=True)
    Name = Column(String,nullable = False)
    Surname = Column(String,nullable = False)
    date = Column(TIMESTAMP(timezone=True),server_default=text('now()'))
    password=Column(String,nullable=False)
    
    
class Grade_Table(Base):
    __tablename__ = "Grade Table"
    teacher_id = Column(Integer,ForeignKey("user.id", ondelete="CASCADE"), nullable = False)
    student_name = Column(String, nullable = False, primary_key = True)
    math = Column(Integer, nullable = False)
    physics = Column(Integer, nullable = False)
    chemistry = Column(Integer, nullable = False)
    
    owner = relationship("Teacher")
