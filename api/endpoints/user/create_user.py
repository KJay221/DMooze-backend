from fastapi.responses import PlainTextResponse
from loguru import logger
from passlib.context import CryptContext

from db import SESSION
from models import User

from .model import UserCreate


def create_user(user_create_input: UserCreate):
    try:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        hashed_password = pwd_context.hash(user_create_input.password)
        SESSION.add(
            User(
                **{
                    "account": user_create_input.account,
                    "hashed_password": hashed_password,
                    "money": 1000,
                    "is_platform": False,
                }
            )
        )
        SESSION.commit()
        return PlainTextResponse("OK", 200)
    except Exception as error:
        SESSION.rollback()
        logger.error(error)
        return PlainTextResponse("Bad Request", 400)
