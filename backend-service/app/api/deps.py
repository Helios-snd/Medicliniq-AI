from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.repo.user import get_user_by_id
from app.db.session import SessionLocal
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)

        user_id = payload.get("user_id")
        email = payload.get("email")

        if not user_id or not email:
            raise credentials_exception

    except ValueError:
        raise credentials_exception

    user = get_user_by_id(db, user_id=user_id)

    if user is None or user.email != email:
        raise credentials_exception

    return user