from src.application.interfaces import (
    AbstractUnitOfWork,
)

from .dto import HelloUserInput, HelloUserOutput

class HelloUserUseCase:
    def __init__(
        self,
        uow: AbstractUnitOfWork,
    ):
        self.uow = uow

    async def execute(self, input_dto: HelloUserInput) -> HelloUserOutput:
        user_name = input_dto.first_name

        

        return HelloUserOutput(user_name, 'testmsg')
