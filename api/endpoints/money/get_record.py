from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from models import MoneyList, Proposal

from .model import RecordReturn


def get_record(proposal_addr: str):
    try:
        money_record = (
            SESSION.query(MoneyList)
            .filter(MoneyList.proposal_addr == proposal_addr)
            .all()
        )
        current_price = 0
        for item in money_record:
            current_price += item.money
        record_return = RecordReturn(
            **{
                "current_price": current_price,
                "target_price": SESSION.query(Proposal)
                .filter(Proposal.proposal_addr == proposal_addr)
                .first()
                .target_price,
            }
        )
        return record_return
    except Exception as error:
        logger.error(error)
        SESSION.rollback()
        return PlainTextResponse("Bad Request or proposal_addr isn't existed", 400)
