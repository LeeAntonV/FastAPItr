from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    database_hostname: Optional[str]
    database_port:  Optional[int]
    database_password: Optional[str]
    database_name:  Optional[str]
    database_username:  Optional[str]
    secret_key:  Optional[str]
    algorithm:  Optional[str]
    access_token_expire_minutes: Optional[int]

    class Config:
        env_file = ".env"


settings = Settings()

