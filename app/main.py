from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from . import models
from .database import engine
from .Routers import create_student, user_login, grade_table


app = FastAPI()


models.Base.metadata.create_all(bind=engine)

    
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(create_student.router)
app.include_router(user_login.router)
app.include_router(grade_table.router)


@app.get("/")
def root():
    return "Main page"

