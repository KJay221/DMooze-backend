from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from models import MoneyList

from .model import MoneyRecord


def add_record(add_record_input: MoneyRecord):
    try:
        new_money_record = MoneyList(
            **{
                "money": add_record_input.money,
                "proposal_addr": add_record_input.proposal_addr,
            }
        )
        SESSION.add(new_money_record)
        SESSION.commit()
        return PlainTextResponse("successfully add record", 200)
    except Exception as error:
        logger.error(error)
        SESSION.rollback()
        return PlainTextResponse("Bad Request or proposal_addr isn't existed", 400)
