import json
import asyncio

from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from currency.currency import settings
from currency.currency.controller import CurrencyController


async def start_consumer() -> AIOKafkaConsumer:
    consumer = AIOKafkaConsumer(
        settings.CONSUME_TOPIC,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
    )
    await consumer.start()
    return consumer


async def start_producer() -> AIOKafkaProducer:
    producer = AIOKafkaProducer(bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    return producer


async def main() -> None:
    controller = CurrencyController()
    consumer = await start_consumer()
    producer = await start_producer()
    try:
        async for message in consumer:
            decoded_message = json.loads(message.value)
            currency_info = await controller.get_currency_info(
                currency_char_code=decoded_message.get("currency_char_code"),
            ) or dict()
            currency_info["telegram_id"] = decoded_message["telegram_id"]
            info_to_send = json.dumps(currency_info).encode(encoding="utf-8")
            await producer.send(topic=settings.PRODUCE_TOPIC, value=info_to_send)
    finally:
        await consumer.stop()
        await producer.stop()


if __name__ == '__main__':
    asyncio.run(main())
