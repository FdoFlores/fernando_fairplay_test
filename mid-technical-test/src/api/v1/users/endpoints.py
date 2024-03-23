
from fastapi import APIRouter, HTTPException, Depends

from db.session import get_session
from sqlalchemy.orm import Session
from .services import User, get_current_user, get_user, hash_password, create_access_token, verify_password
from .schemas import UserSchema

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.post("/create")
async def create_user(user: UserSchema, db : Session = Depends(get_session)):
    db_user = get_user(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    password = hash_password(user.password)

    db_user = User(username=user.username, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"message": "User created successfully", "username": db_user.username}

@router.post("/token")
async def login(user: UserSchema, db: Session = Depends(get_session)):
    db_user = get_user(db, user.username)
    db.close()
    if db_user and verify_password(user.password, db_user.password):
        access_token = create_access_token(user.username)
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Incorrect username or password")