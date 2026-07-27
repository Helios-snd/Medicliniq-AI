from sqlalchemy.orm import Session

from app.models.user import User


def get_user_by_email(db: Session, *, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, *, user_id: str) -> User | None:
    return db.query(User).filter(User.id == user_id).first()


def create_user(
    db: Session,
    *,
    full_name: str,
    email: str,
    phone_number: str,
    hashed_password: str
) -> User:
    
    user = User(
        full_name=full_name,
        email=email,
        phone_number=phone_number,
        hashed_password=hashed_password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
    