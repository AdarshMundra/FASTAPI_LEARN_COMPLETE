from passlib.context import CryptContext # type: ignore

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():
    def bcrypt(password):
        return pwd_context.hash(password)
    
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)