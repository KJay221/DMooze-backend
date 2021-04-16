from fastapi.responses import PlainTextResponse
from loguru import logger
# pylint: disable=E0611
from pydantic import BaseModel

from db import SESSION
from models import Fruit


class Payload(BaseModel):
    name: str


DOC = {
    200: {
        "description": "API response successfully",
        "content": {"text/plain": {"example": "OK"}},
    },
    400: {
        "description": "Object not exists or encounter DB connection issues",
        "content": {"text/plain": {"example": "Bad Request"}},
    },
}


def delete(payload: Payload):
    try:
        fruit: Fruit = SESSION.query(Fruit).filter(Fruit.name == payload.name).one()
        SESSION.delete(fruit)
        SESSION.commit()
        return PlainTextResponse("OK", 200)
    except Exception as error:
        SESSION.rollback()
        logger.error(error)
        return PlainTextResponse("Bad Request", 400)
