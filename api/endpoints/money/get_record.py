from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from models import MoneyList, Proposal

from .model import RecordReturn


def get_record(proposal_id: int):
    try:
        money_record = (
            SESSION.query(MoneyList).filter(MoneyList.proposal_id == proposal_id).all()
        )
        current_price = 0
        for item in money_record:
            current_price += item.money
        record_return = RecordReturn(
            **{
                "current_price": current_price,
                "target_price": SESSION.query(Proposal)
                .filter(Proposal.proposal_id == proposal_id)
                .first()
                .target_price,
            }
        )
        return record_return
    except Exception as error:
        logger.error(error)
        SESSION.rollback()
        return PlainTextResponse("Bad Request or proposal_id isn't existed", 400)
