from __future__ import annotations
from typing import TYPE_CHECKING
from fastapi import FastAPI, Depends
from web.app.schemas import Message
from web.app.producer import get_producer
import json

if TYPE_CHECKING:
    from web.app.producer import AIOWebProducer


app = FastAPI()


@app.post("/currency-info")
async def send(message: Message, producer: AIOWebProducer = Depends(get_producer)) -> None:
    message_to_produce = json.dumps(message.model_dump()).encode(encoding="utf-8")
    await producer.send(value=message_to_produce)
