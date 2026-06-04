from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import get_current_user
from app.database import get_session
from app.schemas.auth import UserResponse, RegisterRequest, TokenResponse, LoginRequest
from app.services.auth import register_user, login_user
from app.models.user import User

router = APIRouter(prefix='/auth', tags=["Auth"])

@router.post('/register', response_model=UserResponse)
async def register(
    data: RegisterRequest,
    db: AsyncSession = Depends(get_session)
    ):
    return await register_user(db, data)


@router.post('/login', response_model=TokenResponse)
async def login(
    data: LoginRequest,
    db: AsyncSession = Depends(get_session)
):
    return await login_user(db, data)


@router.get('/me', response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user