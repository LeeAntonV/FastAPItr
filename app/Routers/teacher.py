from .. import models,schemas,utils,oauth2
from fastapi import status,Depends,APIRouter
from ..database import get_db   
from sqlalchemy.orm import Session
from .. import models,schemas,utils
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError


router = APIRouter(tags=["Teacher_CRUD"])


@router.post("/create_teacher",status_code=status.HTTP_201_CREATED,response_model=schemas.TeacherOut)
async def create_teacher(teacher:schemas.Teacher,db: Session = Depends(get_db)):
     try:
         hashed_password = utils.hash(teacher.password)
         teacher.password = hashed_password
         new_student = models.Teacher(**teacher.dict()) 
         db.add(new_student)
         db.commit()
         return teacher
     except IntegrityError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Student not found')

    

@router.put('/update_teacher{id}',response_model=schemas.TeacherOut)
async def update_teacher(id:int,teacher:schemas.Teacher,db: Session = Depends(get_db)):
    try:
        updated_student = db.query(models.Teacher).filter(models.Teacher.id == id) 
        updated_student.update(teacher.dict(),synchronize_session=False)
        db.commit()
        return updated_student.first()
    except Exception as err:
        return err
    

@router.delete('/delete_teacher/{id}',status_code=status.HTTP_202_ACCEPTED)
async def delete_teacher(id:int,db: Session = Depends(get_db)):
       stud = db.query(models.Teacher).filter(models.Teacher.id == id)

       if stud.first()==None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Student not found')

       stud.delete(synchronize_session=False)
       db.commit()
       return 'Student was deleted' 


@router.get('/teacher/{Name}',response_model=schemas.Teacher)
async def get_teacher_by_name(Name:str,db: Session = Depends(get_db)):
    try:
        stud = db.query(models.Teacher).filter(models.Teacher.Name == Name).all()
        return stud
    except Exception as err:
        return err

    
@router.get('/find_teacher_by_id/{id}',response_model=schemas.Teacher)
async def get_student_by_id(id:int,db: Session = Depends(get_db)):
    try:
        stud = db.query(models.Teacher).filter(models.Teacher.id == id).first()
        return stud
    except Exception as err:
        return err
