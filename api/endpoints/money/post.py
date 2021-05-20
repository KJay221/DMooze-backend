import uuid
from datetime import datetime, timedelta

import pytz
from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from models import MoneyList

from .model import MoneyRecord


def post(add_record_input: MoneyRecord):
    try:
        new_money_record = MoneyList(
            **{
                "id": str(uuid.uuid4()),
                "money": add_record_input.money,
                "proposal_id": add_record_input.proposal_id,
                "sponsor_addr": add_record_input.sponsor_addr,
                "transaction_hash": add_record_input.transaction_hash,
                "input_time": datetime.now(pytz.utc) + timedelta(hours=8),
            }
        )
        SESSION.add(new_money_record)
        SESSION.commit()
        return PlainTextResponse("successfully add record", 200)
    except Exception as error:
        logger.error(error)
        SESSION.rollback()
        return PlainTextResponse("Bad Request or proposal_id isn't existed", 400)
