from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from models import Proposal


def get_page_number():
    try:
        row_number = SESSION.query(Proposal).count()
        page_number = row_number // 9 + 1
        return PlainTextResponse(str(page_number), 200)
    except Exception as error:
        logger.error(error)
        return PlainTextResponse("Bad Request", 400)
