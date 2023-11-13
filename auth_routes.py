from fastapi import APIRouter, HTTPException, status
from werkzeug.security import generate_password_hash

from database import Session, engine
from schemas import SignUpModel
from models import User

auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

session = Session(bind=engine)


@auth_router.get("/")
async def hello():
    return {"message": "Hello"}


@auth_router.post(
    "/signup",
    response_model=SignUpModel,
    status_code=status.HTTP_201_CREATED
)
async def signup(user: SignUpModel):
    db_email = session.query(User).filter(User.email == user.email).first()

    if db_email is not None:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with the email already exists."
        )

    db_username = session.query(User).filter(User.username == user.username).first()

    if db_username is not None:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with the username already exists."
        )

    new_user = User(
        username = user.username,
        email = user.email,
        password = generate_password_hash(user.password),
        is_active = user.is_active,
        is_staff = user.is_staff,
    )

    session.add(new_user)
    session.commit()

    return new_user
