from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse
from app.core.security import hash_password, verify_password, create_access_token
from app.models.user import User
from app.models.organization import Organization
from app.models.membership import Membership



async def register_user(db: AsyncSession, data: RegisterRequest) -> User:
    result = await db.execute(select(User).where(User.email == data.email))
    user_result = result.scalar_one_or_none()

    if user_result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exsists")
    
    hashed_password = hash_password(data.password)

    user = User(
        email=data.email,
        hashed_password=hashed_password,
        full_name=data.full_name,
    )

    org = Organization(
        name = data.org_name,
        slug = data.org_name.lower().replace(" ", "-")
    )
    
    try:
        db.add(user)
        db.add(org)
        await db.flush()

        member = Membership(
        user_id = user.id,
        org_id = org.id,
        role = 'owner'
        )

        db.add(member)
        await db.commit()
        await db.refresh(user)
        return user
    except:
        await db.rollback()
        raise


async def login_user(db: AsyncSession, data: LoginRequest) -> TokenResponse:
    result = await db.execute(select(User).where(User.email == data.email))
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Password or email invalid")
    
    if verify_password(password=data.password, hashed_password=user.hashed_password):
        token = create_access_token(
            {"sub": str(user.id)}
        )
        return TokenResponse(access_token=token)
    
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Password or email invalid")