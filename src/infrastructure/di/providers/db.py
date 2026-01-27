from typing import AsyncGenerator
from dishka import Provider, Scope, provide
from src.infrastructure.db.engine import create_engine
from src.infrastructure.db.session import create_session_factory
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncEngine,
    AsyncSession,
)
from src.core.settings.database import DatabaseSettings

from src.infrastructure.persistence.unit_of_work import SqlAlchemyUnitOfWork
from src.application.interfaces import AbstractUnitOfWork


class DbProvider(Provider):
    @provide(scope=Scope.APP)
    def engine(self, db_settings: DatabaseSettings) -> AsyncEngine:
        return create_engine(db_settings)

    @provide(scope=Scope.APP)
    def session_factory(
        self, engine: AsyncEngine
    ) -> async_sessionmaker[AsyncSession]:
        return create_session_factory(engine)

    # @provide(scope=Scope.REQUEST)
    # def session(
    #     self, session_factory: "async_sessionmaker[AsyncSession]"
    # ) -> AsyncSession:
    #     return session_factory()
    
    
    @provide(scope=Scope.REQUEST)
    async def session(
        self, session_factory: async_sessionmaker[AsyncSession]
    ) -> AsyncGenerator[AsyncSession, None]:
        async with session_factory() as session:
            yield session


    uow = provide(
        SqlAlchemyUnitOfWork,
        provides=AbstractUnitOfWork,
        scope=Scope.REQUEST,
    )

    @provide(scope=Scope.APP)
    async def engine_shutdown(self, engine: AsyncEngine) -> AsyncGenerator[None, None]:
        try:
            yield
        finally:
            await engine.dispose()
