from sqlalchemy import String, Boolean, func, DateTime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from uuid import UUID, uuid4
from datetime import datetime

from app.database import Base


class Organization(Base):
    __tablename__= "organizations"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    slug: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    memberships: Mapped[list["Membership"]] = relationship(back_populates="organization")

