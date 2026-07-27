import uuid
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.health_profile import HealthProfile
from app.repo.health_profile import get_health_profile_by_user_id, create_health_profile, update_health_profile
from app.schemas.health_profile import HealthProfileCreate, HealthProfileUpdate


def create_profile(db:Session, *, user_id: uuid.UUID, payload: HealthProfileCreate)->HealthProfile :
    existing_profile = get_health_profile_by_user_id(db, user_id=user_id,)
    if existing_profile:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "Health profile already exist"
        )

    profile = HealthProfile(
        user_id = user_id,
        date_of_birth = payload.date_of_birth,
        gender = payload.gender,
        blood_group = payload.blood_group,
        height_cm = payload.height_cm,
        weight_kg = payload.weight_kg,
        emergency_contact_name = payload.emergency_contact_name,
        emergency_contact_number = payload.emergency_contact_number
    )
    return create_health_profile(
        db,
        profile = profile
    )


def get_profile(
    db: Session,
    *,
    user_id: uuid.UUID,
) -> HealthProfile:
        profile = get_health_profile_by_user_id(db, user_id=user_id)
        if not profile:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Health profile not found",
            )
    
        return profile


def update_profile(
    db: Session,
    *,
    user_id: uuid.UUID,
    payload: HealthProfileUpdate,
) -> HealthProfile:    
        profile = get_health_profile_by_user_id(db, user_id=user_id)
        if not profile: 
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Health profile not found"
            )
    
        update_data = payload.model_dump(
            exclude_unset = True 
        )
    
        for field, value in update_data.items():
            setattr(profile, field, value)
    
        
        return update_health_profile(
            db,
            profile=profile
        )


