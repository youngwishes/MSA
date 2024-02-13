from pydantic import BaseModel


class Message(BaseModel):
    currency_char_code: str
    telegram_id: int
