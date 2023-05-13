from passlib.context import CryptContext

pswdecr = CryptContext(schemes=['bcrypt'], deprecated="auto")

def hash(password:str):
    return pswdecr.hash(password)


def verify(plain_password, hashed_password):
    return pswdecr.verify(plain_password, hashed_password)
