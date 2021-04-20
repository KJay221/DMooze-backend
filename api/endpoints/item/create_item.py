from fastapi import Header
from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from endpoints.user.user_login import confirm_token
from models import Item

from .model import ItemCreate


def create_item(create_item_input: ItemCreate, token: str = Header(None)):
    try:
        db_user = confirm_token(token)
        new_item = Item(
            **{
                "owner_id": db_user.id,
                "target_price": create_item_input.target_price,
                "project_content": create_item_input.project_content,
                "start_time": create_item_input.start_time,
                "end_time": create_item_input.end_time,
                "project_name": create_item_input.project_name,
                "representative": create_item_input.representative,
                "email": create_item_input.email,
                "phone": create_item_input.phone,
            }
        )
        SESSION.add(new_item)
        SESSION.commit()
        return PlainTextResponse("successfully create", 200)
    except Exception as error:
        logger.error(error)
        return PlainTextResponse("Bad Request or token is invalid", 400)
