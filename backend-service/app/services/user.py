from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.core.security import create_access_token
from app.repo.user import create_user, get_user_by_email
from app.schemas.user import TokenResponse, UserLoginRequest, UserSignupRequest, UserSignupResponse
from app.utils.hashing import get_password_hash, verify_password


def register_user(db:Session, payload:UserSignupRequest) -> UserSignupResponse:
    existing_user = get_user_by_email(db, email = payload.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Email already exists')

    hashed_password = get_password_hash(payload.password)
    user = create_user(db, full_name= payload.full_name, email = payload.email, phone_number=payload.phone_number, hashed_password=hashed_password)
    return UserSignupResponse(message='User created sucessfully', user_id = user.id)


def login_user(db:Session, payload:UserLoginRequest) -> TokenResponse:
    user = get_user_by_email(db, email=payload.email)
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    access_token = create_access_token(user_id=str(user.id), email=user.email)
    return TokenResponse(access_token=access_token)

    