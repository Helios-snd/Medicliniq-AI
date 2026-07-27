import uuid
from sqlalchemy.orm import Session
from app.models.health_profile import HealthProfile

def get_health_profile_by_user_id(db: Session, *, user_id: uuid.UUID) -> HealthProfile | None:
    return(
        db.query(HealthProfile).filter(HealthProfile.user_id == user_id).first()
    )


def create_health_profile(db: Session, *, profile: HealthProfile) -> HealthProfile:
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile


def update_health_profile(
    db: Session,
    *,
    profile: HealthProfile
) -> HealthProfile:
    db.commit()
    db.refresh(profile)

    return profile

