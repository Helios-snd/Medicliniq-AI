import uuid
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class DoctorCreate(BaseModel):
    name: str
    specialization: str
    hospital: str
    phone_number: str
    email: str


class DoctorUpdate(BaseModel):
    hospital: str | None = None
    phone_number: str | None = None
    email : str | None = None


class DoctorResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    name: str
    specialization: str
    hospital: str
    phone_number: str | None
    email: str | None
    created_at: datetime
    updated_at: datetime

