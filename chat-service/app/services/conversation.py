from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from app.schemas.conversation import ConversationCreate
from app.schemas.message import MessageCreate
from app.models.conversation import Conversation
from app.models.message import Message


async def create_conversation(db: AsyncSession, data: ConversationCreate, org_id: UUID) -> Conversation:
    conversation  = Conversation(
        visitor_id = data.visitor_id,
        visitor_name = data.visitor_name,
        visitor_email = data.visitor_email,
        org_id = org_id
    )

    try:
        db.add(conversation )
        await db.commit()
        await db.refresh(conversation)

        return conversation 
    except:
        await db.rollback()
        raise


async def get_conversation(db: AsyncSession, conversation_id: UUID, org_id: UUID) -> Conversation:
    result = await db.execute(
        select(Conversation).where(Conversation.id == conversation_id, Conversation.org_id == org_id)
    )
    conversation = result.scalar_one_or_none()

    if conversation is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Converstation not found")
    
    return conversation

async def get_conversations(db: AsyncSession, org_id: UUID) -> list[Conversation]:
    result = await db.execute(
    select(Conversation).where(Conversation.org_id == org_id)
    )
    return result.scalars().all()


async def save_message(db: AsyncSession, conversation_id: UUID, org_id: UUID, data: MessageCreate) -> Message:
    message = Message(
        conversation_id=conversation_id,
        org_id=org_id,
        role=data.role,
        content=data.content
    )

    try:
        db.add(message )
        await db.commit()
        await db.refresh(message)

        return message 
    except:
        await db.rollback()
        raise