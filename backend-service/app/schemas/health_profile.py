import uuid
from datetime import datetime, date
from pydantic import BaseModel, ConfigDict


class HealthProfileCreate(BaseModel):
    date_of_birth : date
    gender : str
    blood_group : str
    height_cm : float
    weight_kg : float
    emergency_contact_name : str | None = None
    emergency_contact_number : str | None = None


class HealthProfileUpdate(BaseModel):
    height_cm : float | None = None
    weight_kg : float | None = None
    emergency_contact_name : str | None = None
    emergency_contact_number : str | None = None


class HealthProfileResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : uuid.UUID
    user_id : uuid.UUID
    date_of_birth : date
    gender : str
    blood_group : str
    height_cm : float
    weight_kg : float
    emergency_contact_name : str | None = None
    emergency_contact_number : str | None = None
    created_at : datetime
    updated_at : datetime

