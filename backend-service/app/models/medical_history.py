import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class MedicalHistory(Base):
    __tablename__ = "medical_histories"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    chronic_conditions: Mapped[list[str] | None] = mapped_column(
        ARRAY(String),
        nullable=True,
    )

    past_surgeries: Mapped[list[str] | None] = mapped_column(
        ARRAY(String),
        nullable=True,
    )

    family_history: Mapped[list[str] | None] = mapped_column(
        ARRAY(String),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )