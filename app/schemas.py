from pydantic import BaseModel,EmailStr
from typing import Optional


class StudentOut(BaseModel):
    Name :Optional[str]
    Surname: Optional[str]
    email:Optional[EmailStr]
    
    class Config:
        orm_mode = True

class Student(StudentOut):
    Name :Optional[str]
    Surname: Optional[str]
    email:Optional[EmailStr]
    password:Optional[str]

    class Config:
        orm_mode = True
    

class Token(BaseModel):
    access_token: Optional[str]
    token_type: Optional[str]
    
    class Config:
        orm_mode = True

class TokenData(BaseModel):
    id: Optional[str] = None



class Table(BaseModel):
    teacher_id: Optional[int]
    student_name: Optional[str]
    math:  Optional[int]
    physics:  Optional[int]
    chemistry:  Optional[int]

    class Config:

        orm_mode = True
