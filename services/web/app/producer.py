from aiokafka import AIOKafkaProducer
from web.app import settings
import asyncio

event_loop = asyncio.get_event_loop()


class AIOWebProducer(object):
    def __init__(self):
        self.__producer = AIOKafkaProducer(
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
            loop=event_loop,
        )
        self.__produce_topic = settings.PRODUCE_TOPIC

    async def start(self) -> None:
        await self.__producer.start()

    async def stop(self) -> None:
        await self.__producer.stop()

    async def send(self, value: bytes) -> None:
        await self.start()
        try:
            await self.__producer.send(
                topic=self.__produce_topic,
                value=value,
            )
        finally:
            await self.stop()


def get_producer() -> AIOWebProducer:
    return AIOWebProducer()
