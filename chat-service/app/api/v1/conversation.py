from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.database import get_session
from app.schemas.conversation import ConversationCreate, ConversationResponse
from app.services.conversation import create_conversation, get_conversation, get_conversations

router = APIRouter(prefix="/conversations", tags=["Conversations"])

test_org_id = UUID("00000000-0000-0000-0000-000000000001")


@router.post("/", response_model=ConversationResponse)
async def create(
    data: ConversationCreate,
    db: AsyncSession = Depends(get_session)
):
    return await create_conversation(db, data, test_org_id)


@router.get("/", response_model=list[ConversationResponse])
async def get_list(
    db: AsyncSession = Depends(get_session)
):
    return await get_conversations(db, test_org_id)


@router.get("/{conversation_id}", response_model=ConversationResponse)
async def get_one(
    conversation_id: UUID,
    db: AsyncSession = Depends(get_session)
):
    return await get_conversation(db, conversation_id, test_org_id)