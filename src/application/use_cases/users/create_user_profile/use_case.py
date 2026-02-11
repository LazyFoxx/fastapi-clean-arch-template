import structlog

from src.application.interfaces import AbstractUnitOfWork


class CreateUserProfileUseCase:
    def __init__(
        self,
        uow: AbstractUnitOfWork,
    ):
        self.uow = uow
        self.logger = structlog.get_logger(__name__)

    async def execute(self, user_id: str) -> None:
        # new_user = User(
        #     id=UUID(user_id),
        #     first_name="",
        #     last_name="",
        #     avatar_url="",
        #     bio="",
        # )
        """и другая логика"""
        pass
