from dishka import Provider, Scope, provide
from src.application.use_cases import (
    HelloUserUseCase
)


class UseCaseProvider(Provider):
    hello_user = provide(HelloUserUseCase, scope=Scope.REQUEST)
