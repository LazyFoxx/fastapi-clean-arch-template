from contextlib import asynccontextmanager
from typing import AsyncGenerator

from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.infrastructure.di.container import get_container
from src.presentation.api.exception_handlers import setup_exception_handlers
from src.presentation.api.routers.root import api_router

container = get_container()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # startup
    yield
    # shutdown
    await container.close()


app = FastAPI(lifespan=lifespan)
setup_dishka(container, app=app)
setup_exception_handlers(app)

app.include_router(api_router)
