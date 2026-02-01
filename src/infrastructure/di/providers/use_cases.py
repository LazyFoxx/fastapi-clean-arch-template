from dishka import Provider, Scope, provide

from src.application.use_cases import GetUserProfileUseCase


class UseCaseProvider(Provider):
    hello_user = provide(GetUserProfileUseCase, scope=Scope.REQUEST)
