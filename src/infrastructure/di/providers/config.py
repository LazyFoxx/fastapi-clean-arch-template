from dishka import FromDishka, Provider, Scope, provide
from src.core.settings import (
    DatabaseSettings,
    RedisSettings,
)

class ConfigProvider(Provider):
    # Целые объекты настроек
    @provide(scope=Scope.APP)

    @provide(scope=Scope.APP)
    def db_settings(self) -> DatabaseSettings:
        return DatabaseSettings()

    @provide(scope=Scope.APP)
    def redis_settings(self) -> RedisSettings:
        return RedisSettings()

