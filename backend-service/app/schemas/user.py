import uuid
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, EmailStr

class UserSignupRequest(BaseModel):
    full_name : str
    email : EmailStr
    phone_number : str
    password : str = Field(min_length=8, max_length=128)


class UserLoginRequest(BaseModel):
    email : EmailStr
    password : str


class UserSignupResponse(BaseModel):
    message : str
    user_id : uuid.UUID    


class TokenResponse(BaseModel):
    access_token : str
    token_type : str = "bearer"


class UserInDB(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    email: EmailStr
    created_at: datetime
