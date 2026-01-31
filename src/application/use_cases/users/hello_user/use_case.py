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
        user_name = input_dto.first_name

        self.uow.users.get_by_id(user_id)

        

        return GetProfileUserOutput(user_name, 'testmsg')
