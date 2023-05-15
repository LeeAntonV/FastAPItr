import pytest
import os

from dotenv.main import dotenv
from jose import jwt
from app import schemas

from app.config import settings

local_dotenv()

def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "test_email@gmail.com", "password": "password123"})

    new_user = schemas.StudentOut(**res.json())
    assert new_user.email == "test_email@gmail.com"
    assert res.status_code == 201


def test_login_user(test_user, client):
    res = client.post(
        "/login", data={"username": test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token,
                         os.getenv.get("SECRET_KEY"), algorithms=[os.getenv.get("ALGORITHM")])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200
