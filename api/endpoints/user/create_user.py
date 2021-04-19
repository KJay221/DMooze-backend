from fastapi.responses import PlainTextResponse
from loguru import logger
from passlib.context import CryptContext

from db import SESSION
from models import User

from .model import UserBase


def create_user(create_user_input: UserBase):
    try:
        if (
            not SESSION.query(User)
            .filter(User.account == create_user_input.account)
            .first()
        ):
            pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
            hashed_password = pwd_context.hash(create_user_input.password)
            SESSION.add(
                User(
                    **{
                        "account": create_user_input.account,
                        "hashed_password": hashed_password,
                        "money": 1000,
                        "is_platform": False,
                    }
                )
            )
            SESSION.commit()
            return PlainTextResponse("OK", 200)
        return PlainTextResponse("User already exist", 400)
    except Exception as error:
        SESSION.rollback()
        logger.error(error)
        return PlainTextResponse("Bad Request", 400)
