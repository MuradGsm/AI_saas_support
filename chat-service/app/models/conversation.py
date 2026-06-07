from sqlalchemy import String, ForeignKey, DateTime, func, UUID as sql_uuid
from sqlalchemy.orm import mapped_column, Mapped, relationship
from uuid import UUID, uuid4
from datetime import datetime

from app.database import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4, index=True)
    org_id: Mapped[UUID] = mapped_column(sql_uuid, nullable=False, index=True)

    channel: Mapped[str] = mapped_column(String, default='widget')
    visitor_id: Mapped[str] = mapped_column(String, nullable=False)
    visitor_name: Mapped[str] = mapped_column(String, nullable=True)
    visitor_email: Mapped[str] = mapped_column(String, nullable=True)

    status: Mapped[str] = mapped_column(default='active')
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] =mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    messages: Mapped[list["Message"]] = relationship(back_populates='conversations')