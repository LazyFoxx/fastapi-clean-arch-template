from dishka import make_async_container

from .providers import (
    ConfigProvider,
    DbProvider,
    RedisProvider,
    UseCaseProvider,
    AuthProvider,
)

# Список всех провайдеров
_PROVIDERS = [
    ConfigProvider(),
    DbProvider(),
    RedisProvider(),
    UseCaseProvider(),
    AuthProvider(),
]


def get_container():
    """
    Фабрика для создания Dishka контейнера.
    Вызывается только при старте приложения (в lifespan) или в тестах.
    """
    return make_async_container(*_PROVIDERS)
