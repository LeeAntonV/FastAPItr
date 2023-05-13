from fastapi import APIRouter,status,HTTPException, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import database, schemas, models, utils, oauth2
from sqlalchemy.orm import Session


router = APIRouter(tags=["AUTHENTIFICATION"])


@router.post('/login', response_model=schemas.Token)
async def login(user_credentials:OAuth2PasswordRequestForm=Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.Students).filter(models.Students.email == user_credentials.username).first()

    if not user:
        raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,detail="Invalid user"
                  )
    access_token = oauth2.create_access_token(data={"user_id":user.id})


    return  access_token
