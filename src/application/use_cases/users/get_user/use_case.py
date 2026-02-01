from src.application.exceptions import UserNotFoundError
from src.application.interfaces import (
    AbstractUnitOfWork,
)

from .dto import GetProfileserInput, GetProfileUserOutput


class GetUserProfileUseCase:
    def __init__(
        self,
        uow: AbstractUnitOfWork,
    ):
        self.uow = uow

    async def execute(self, input_dto: GetProfileserInput) -> GetProfileUserOutput:
        async with self.uow:
            user = await self.uow.users.get_by_id(input_dto.user_id)

        if user is None:
            raise UserNotFoundError()

        return GetProfileUserOutput(
            first_name=user.first_name,
            last_name=user.last_name,
            avatar_url=user.avatar_url,
            bio=user.bio,
        )
