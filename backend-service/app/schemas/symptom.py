import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SymptomCreate(BaseModel):
    symptom_name: str
    severity: str
    duration: str
    notes: str | None = None


class SymptomUpdate(BaseModel):
    severity: str | None = None
    duration: str | None = None
    notes: str | None = None


class SymptomResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: uuid.UUID
    user_id: uuid.UUID

    symptom_name: str
    severity: str
    duration: str
    notes: str | None

    created_at: datetime
    updated_at: datetime