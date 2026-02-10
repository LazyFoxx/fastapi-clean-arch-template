# rabbit/consumer.py (в consumer-сервисе)
import json
from typing import Awaitable, Callable

import structlog
from aio_pika import IncomingMessage

from .connection import RabbitConnection

logger = structlog.get_logger(__name__)


class RabbitConsumer:
    def __init__(self, connection: RabbitConnection):
        self._connection = connection
        self.logger = structlog.get_logger(__name__)
        self._running = False

    async def start_consuming(
        self,
        queue_name: str,
        callback: Callable[[IncomingMessage], Awaitable[None]],
    ) -> None:
        """
        Запускает потребление из очереди.
        :param queue_name: Имя очереди (e.g., "register_user")
        :param callback: Async функция для обработки сообщений (async def process_message(message: IncomingMessage))
        """
        try:
            channel = self._connection.channel

            # Получаем очередь (она уже настроена в topology)
            queue = await channel.get_queue(queue_name)

            # Запускаем потребление
            self._running = True
            async with queue.iterator() as queue_iter:
                async for message in queue_iter:
                    if not self._running:
                        break
                    try:
                        await callback(message)
                    except Exception as e:
                        self.logger.error(
                            "Ошибка обработки сообщения", error=str(e), exc_info=True
                        )
                        await message.nack(
                            requeue=True
                        )  # Перезапуск в очередь при ошибке

            self.logger.info(f"Consumer stopped for queue {queue_name}")

        except Exception as e:
            self.logger.error("Ошибка запуска consumer", error=str(e), exc_info=True)
            raise

    async def stop_consuming(self) -> None:
        self._running = False


# Callback: Обрабатывает сообщение, извлекает user_id и вызывает Use Case
async def process_user_registered(
    message: IncomingMessage,
    # use_case: ExempleUseCase,  # Инжектируем Use Case как зависимость!
) -> None:
    async with message.process(ignore_processed=True):  # Авто-ack/nack
        try:
            payload = json.loads(message.body.decode())
            user_id = payload.get(
                "user_id"
            )  # Предполагаем, что в payload есть {"user_id": 123}

            if not user_id:
                raise ValueError("No user_id in payload")

            logger.info(
                "Получено сообщение с user_id", user_id=user_id, payload=payload
            )

            # Вызываем Use Case для обработки
            # await use_case.execute(user_id)

            await message.ack()  # Явный ack после успеха

        except Exception as e:
            logger.error("Ошибка обработки сообщения", error=str(e), exc_info=True)
            await message.nack(requeue=True)
