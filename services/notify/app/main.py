from aiogram import Bot
from aiogram import Dispatcher
from aiokafka import AIOKafkaConsumer
from notify.app import settings

import asyncio
import json

dispatcher = Dispatcher()
BOT = Bot(token=settings.BOT_TOKEN)


async def consume() -> None:
    consumer = AIOKafkaConsumer(
        settings.CONSUME_TOPIC,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
    )
    await consumer.start()
    try:
        async for msg in consumer:
            serialized = json.loads(msg.value)
            await BOT.send_message(
                chat_id=serialized.get("telegram_id"),
                text=serialized.get("currency_value") or "Валюта не найдена",
            )
    finally:
        await consumer.stop()


async def main() -> None:
    polling = asyncio.create_task(dispatcher.start_polling(BOT))
    consuming = asyncio.create_task(consume())
    await asyncio.gather(polling, consuming)
    print("Bot has successfully started polling")


if __name__ == "__main__":
    asyncio.run(main())
