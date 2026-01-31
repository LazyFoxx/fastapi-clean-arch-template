from fastapi import APIRouter, Depends, status, BackgroundTasks, Response
from dishka.integrations.fastapi import FromDishka, inject
from src.secure.dependencies import get_current_user
from domain.entities.user.user import User

from src.application.use_cases import (
    HelloUserUseCase
)

router = APIRouter(prefix="/user", tags=["user"])

@router.post(
    "/forgot-password/change-password",
    response_model=LoginResponse,
    status_code=status.HTTP_200_OK,
    summary="Смена пароля пользователем",
    description=("Меняет пароль пользователя в БД на новый и производит автологин."),
    responses={
        200: {
            "model": LoginResponse,
            "description": "Успешная авторизация",
        },
    },
)
@inject
async def change_password(
    payload: NewPasswordRequest,
    use_case: FromDishka[HelloUserUseCase],
    user: User = Depends(get_current_user),
) -> LoginResponse:
    
    return {}
