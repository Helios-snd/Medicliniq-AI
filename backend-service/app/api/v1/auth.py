from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.user import TokenResponse, UserLoginRequest, UserSignupRequest, UserSignupResponse
from app.services.user import login_user, register_user

router = APIRouter()


@router.post("/signup", response_model=UserSignupResponse, status_code=status.HTTP_201_CREATED)
def signup(payload: UserSignupRequest, db: Session = Depends(get_db)) -> UserSignupResponse:
    return register_user(db, payload)


@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
def login(payload: UserLoginRequest, db: Session = Depends(get_db)) -> TokenResponse:
    return login_user(db, payload)
