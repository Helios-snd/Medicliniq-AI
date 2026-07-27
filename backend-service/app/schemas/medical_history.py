import uuid
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class MedicalHistoryCreate(BaseModel):
    chronic_conditions: list[str] = []

    past_surgeries: list[str] =[]
    family_history: list[str] = []


class MedicalHistoryUpdate(BaseModel):
    chronic_conditions: list[str] | None = None
    past_surgeries: list[str] | None = None
    family_history: list[str] | None = None


class MedicalHistoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    user_id: uuid.UUID
    chronic_conditions: list[str] | None 
    past_surgeries: list[str] | None 
    family_history: list[str] | None 
    created_at: datetime
    updated_at: datetime
