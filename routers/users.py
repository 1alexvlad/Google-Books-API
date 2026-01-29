from fastapi import APIRouter, HTTPException
from core.auth import get_password_hash, verify_password

from schemas.users import SUserAuth
from services.users import UsersServices

router = APIRouter(
    prefix='/auth',
    tags=['Auth & Пользователи']
)

@router.post('/register')
async def register_user(user_data: SUserAuth):
    existing_user = await UsersServices.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await UsersServices.add(email=user_data.email, password=hashed_password)


@router.post('/login')
async def login_user(user_data: SUserAuth):
    user = await UsersServices.find_one_or_none(email=user_data.email)
    if not user:
        raise HTTPException(500)
    if user:
        password_is_valid = verify_password(user_data.password, user.password)
        if not password_is_valid:
            raise HTTPException(500)