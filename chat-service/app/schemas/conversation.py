from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

class ConversationCreate(BaseModel):
    visitor_id: str
    visitor_name: str | None
    visitor_email: str | None
    channel: str = "widget"
 

class ConversationResponse(BaseModel):
    id: UUID
    org_id: UUID
    channel: str
    visitor_id: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
