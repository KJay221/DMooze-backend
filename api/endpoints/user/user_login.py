import secrets

import jwt
from fastapi.responses import PlainTextResponse
from loguru import logger
from passlib.context import CryptContext

from db import SESSION
from models import User

from .model import UserBase

SECRET_KEY = secrets.token_hex(32)


def user_login(user_login_input: UserBase):
    try:
        db_user = (
            SESSION.query(User).filter(User.account == user_login_input.account).first()
        )
        psw_is_correct = CryptContext(schemes=["bcrypt"], deprecated="auto").verify(
            user_login_input.password, db_user.hashed_password
        )
        if not db_user or not psw_is_correct:
            return PlainTextResponse("Incorrect account or password", 400)
        to_encode = {"account": user_login_input.account}
        access_token = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as error:
        logger.error(error)
        return PlainTextResponse("Bad Request", 400)


def confirm_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
    db_user = SESSION.query(User).filter(User.account == payload.get("account")).first()
    return db_user
