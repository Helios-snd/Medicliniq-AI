import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class VitalCreate(BaseModel):
    blood_pressure: str
    heart_rate: int
    temperature: float
    oxygen_saturation: int
    weight: float
    height: float


class VitalUpdate(BaseModel):
    blood_pressure: str | None = None
    heart_rate: int | None = None
    temperature: float | None = None
    oxygen_saturation: int | None = None
    weight: float | None = None
    height: float | None = None


class VitalResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: uuid.UUID
    user_id: uuid.UUID

    blood_pressure: str
    heart_rate: int
    temperature: float
    oxygen_saturation: int
    weight: float
    height: float

    recorded_at: datetime
    created_at: datetime
    updated_at: datetime