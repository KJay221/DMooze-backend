from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from models import MoneyList

from .model import MoneyRecord


def post(add_record_input: MoneyRecord):
    try:
        last_id = SESSION.query(MoneyList).order_by(MoneyList.id.desc()).first()
        if not last_id:
            last_id = 1
        else:
            last_id = last_id.id + 1
        new_money_record = MoneyList(
            **{
                "id": last_id,
                "money": add_record_input.money,
                "proposal_id": add_record_input.proposal_id,
                "sponsor_addr": add_record_input.sponsor_addr,
                "transaction_hash": add_record_input.transaction_hash,
            }
        )
        SESSION.add(new_money_record)
        SESSION.commit()
        return PlainTextResponse("successfully add record", 200)
    except Exception as error:
        logger.error(error)
        SESSION.rollback()
        return PlainTextResponse("Bad Request or proposal_id isn't existed", 400)
