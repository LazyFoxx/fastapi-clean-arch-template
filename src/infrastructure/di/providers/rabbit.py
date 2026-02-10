from functools import partial
from typing import Awaitable, Callable

from aio_pika import IncomingMessage
from dishka import Provider, Scope, provide
from dishka.entities.key import DependencyKey

from src.core.settings.rabbit import RabbitSettings
from src.infrastructure.rabbit import (
    RabbitConnection,
    RabbitConsumer,
    RabbitPublisher,
    process_user_registered,
)

USER_REGISTERED = DependencyKey(Callable, "user_registered")


class RabbitProvider(Provider):
    @provide(scope=Scope.APP)
    async def rabbit_connection(self, settings: RabbitSettings) -> RabbitConnection:
        conn = RabbitConnection(settings)
        await conn.connect()  # подключаемся один раз на всё приложение
        await conn.ensure_topology()  # настраиваем топологию
        return conn

    @provide(scope=Scope.APP)
    async def publisher(self, conn: RabbitConnection) -> RabbitPublisher:
        return RabbitPublisher(conn)

    @provide(scope=Scope.APP)
    async def consumer(self, conn: RabbitConnection) -> RabbitConsumer:
        return RabbitConsumer(conn)

    @provide(scope=Scope.APP, provides=USER_REGISTERED)
    def user_registered_callback(
        self,
    ) -> Callable[[IncomingMessage], Awaitable[None]]:
        return partial(process_user_registered)
