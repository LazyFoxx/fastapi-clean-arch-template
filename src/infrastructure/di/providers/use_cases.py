from dishka import Provider, Scope, provide
from src.application.users.hello_user import (
    HelloUserUseCase
)


class UseCaseProvider(Provider):
    hello_user = provide(HelloUserUseCase, scope=Scope.REQUEST)
