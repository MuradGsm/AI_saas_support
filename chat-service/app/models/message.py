from sqlalchemy import String, DateTime, ForeignKey, Text, func, UUID as sql_uuid
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from uuid import UUID, uuid4

from app.database import Base

class Message(Base):
    __tablename__ = 'messages'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4, index=True)
    conversation_id: Mapped[UUID] = mapped_column(ForeignKey("conversations.id"))
    org_id: Mapped[UUID] = mapped_column(sql_uuid, nullable=False)

    role: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    conversations: Mapped['Conversation'] = relationship(back_populates='messages') 