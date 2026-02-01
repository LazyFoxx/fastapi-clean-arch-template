from uuid import UUID

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, Depends, status

from src.application.use_cases import GetUserProfileUseCase
from src.application.use_cases.users.get_user.dto import GetProfileserInput
from src.presentation.api.dependencies.auth import get_current_user_id
from src.presentation.api.dto.v1.users.user import UserProfileResponse

router = APIRouter(prefix="/user", tags=["user"])


@router.post(
    "/get-user-profile",
    response_model=UserProfileResponse,
    status_code=status.HTTP_200_OK,
    summary="Профиль пользователя",
    description=("Возвращает имя, фамилию, ссылку на аватар и т д."),
)
@inject
async def get_user_profile(
    use_case: FromDishka[GetUserProfileUseCase],
    user_id: UUID = Depends(get_current_user_id),
) -> UserProfileResponse:
    dto = GetProfileserInput(user_id=user_id)
    user_profile = await use_case.execute(input_dto=dto)

    return UserProfileResponse(
        first_name=user_profile.first_name,
        last_name=user_profile.last_name,
        avatar_url=user_profile.avatar_url,
        bio=user_profile.bio,
    )
