from app.database import Base
from sqlalchemy import DateTime, String, Boolean, func
from sqlalchemy.orm import mapped_column, Mapped, relationship
from uuid import uuid4, UUID
from datetime import datetime

class User(Base):
    __tablename__="users"

    id: Mapped[UUID] = mapped_column(primary_key=True, index=True, unique=True, default=uuid4)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    
    full_name: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_superadmin: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    memberships: Mapped[list["Membership"]] = relationship(back_populates="user")