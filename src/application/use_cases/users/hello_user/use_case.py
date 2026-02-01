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

        

        return GetProfileUserOutput(**user)
