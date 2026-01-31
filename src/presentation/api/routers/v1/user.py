from fastapi import APIRouter, Depends, status, BackgroundTasks, Response
from dishka.integrations.fastapi import FromDishka, inject
from src.presentation.api.dto.v1.users.user import UserProfileResponse
from src.presentation.api.dependencies.auth import get_current_user
from src.domain.entities import User

from src.application.use_cases import (
    GetUserProfileUseCase
)

router = APIRouter(prefix="/user", tags=["user"])

@router.post(
    "/forgot-password/change-password",
    response_model=UserProfileResponse,
    status_code=status.HTTP_200_OK,
    summary="Смена пароля пользователем",
    description=("Меняет пароль пользователя в БД на новый и производит автологин."),
    responses={
        200: {
            "model": UserProfileResponse,
            "description": "Успешная авторизация",
        },
    },
)
@inject
async def get_user_profile(
    use_case: FromDishka[GetUserProfileUseCase],
    user: User = Depends(get_current_user),
) -> UserProfileResponse:
    user_profile = use_case.execute()
    return UserProfileResponse(**user_profile)
