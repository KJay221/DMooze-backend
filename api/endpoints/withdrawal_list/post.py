from datetime import datetime, timedelta

import pytz
from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from models import WithdrawalList

from .model import WithdrawalRecord


def post(record_input: WithdrawalRecord):
    try:
        last_id = (
            SESSION.query(WithdrawalList).order_by(WithdrawalList.id.desc()).first()
        )
        if not last_id:
            last_id = 1
        else:
            last_id = last_id.id + 1
        new_withdrawal_record = WithdrawalList(
            **{
                "id": last_id,
                "money": record_input.money,
                "proposal_id": record_input.proposal_id,
                "use_description": record_input.use_description,
                "transaction_hash": record_input.transaction_hash,
                "output_time": datetime.now(pytz.utc) + timedelta(hours=8),
            }
        )
        SESSION.add(new_withdrawal_record)
        SESSION.commit()
        return PlainTextResponse("successfully add record", 200)
    except Exception as error:
        logger.error(error)
        SESSION.rollback()
        return PlainTextResponse("Bad Request or proposal_id isn't existed", 400)
