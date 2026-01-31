# from src.application.exceptions import (
#     InvalidTokenError,
# )

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


# async def invalid_token(request: Request, exc: InvalidTokenError):
#     return JSONResponse(
#         status_code=401,
#         headers={"WWW-Authenticate": "Bearer"},
#         content={
#             "message": f"Неверный токен: {exc}",
#         },
#     )


def setup_exception_handlers(app: FastAPI):
    """Единая регистрация всех обработчиков ошибок."""
    # app.add_exception_handler(InvalidTokenError, invalid_token)  # type: ignore[arg-type]
