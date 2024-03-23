from fastapi import HTTPException, Depends
# from comun.models.user import UsersDB
from db.session import get_session
from sqlalchemy.orm import Session
from ..utils import DBSessionContext
from datetime import timedelta, datetime
from jose import JWTError, jwt
from db.models.models import User
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()
SECRET_KEY = "VVWw5z5LctuPvmW7N4l-CtXi1ikem1-0-EPkA1kzVlg"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
import bcrypt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def hash_password(password: str) -> str:
    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    # Return the hashed password as a string
    return hashed_password.decode('utf-8')

def get_user(db_session, username: str):
    return db_session.query(User).filter(User.username == username).first()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_session)):
        token = credentials.credentials
        print(token)
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise HTTPException(status_code=401, detail="Invalid token")
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = get_user(db, username)
        db.close()
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user

def create_access_token(username):
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": username, "exp": expire}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

    # Function to get current user based on JWT token
    