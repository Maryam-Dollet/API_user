from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# default hash algorithm = bcrypt
def hash(password: str):
    return pwd_context.hash(password)
