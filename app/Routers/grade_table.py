from fastapi import APIRouter,Depends,status,HTTPException
from ..database import get_db
from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

router = APIRouter(tags=["Grade_Table"])


@router.post("/student_grade",response_model=schemas.Table,status_code=status.HTTP_201_CREATED)
async def create_table(table:schemas.Table,
                       db: Session = Depends(get_db),
                       current_user:int = Depends(oauth2.get_current_user)):
    try:

        new_table = models.Grade_Table(owner_id=current_user.id,**table.dict())
        db.add(new_table)
        db.commit()
        return new_table
 
    except IntegrityError as err:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = "Table for this student was already created")


