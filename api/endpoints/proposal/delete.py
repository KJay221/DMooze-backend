from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from models import ImageList, MoneyList, Proposal, WithdrawalList


async def delete(proposal_id: int):
    try:
        for element in enumerate(
            SESSION.query(ImageList).filter(ImageList.proposal_id == proposal_id).all()
        ):
            SESSION.delete(element[1])
            SESSION.commit()
        for element in enumerate(
            SESSION.query(WithdrawalList)
            .filter(WithdrawalList.proposal_id == proposal_id)
            .all()
        ):
            SESSION.delete(element[1])
            SESSION.commit()
        for element in enumerate(
            SESSION.query(MoneyList).filter(MoneyList.proposal_id == proposal_id).all()
        ):
            SESSION.delete(element[1])
            SESSION.commit()
        db_proposal = (
            SESSION.query(Proposal).filter(Proposal.proposal_id == proposal_id).first()
        )
        SESSION.delete(db_proposal)
        SESSION.commit()
        return PlainTextResponse("successfully receive fail msg", 200)
    except Exception as error:
        logger.error(error)
        SESSION.rollback()
        return PlainTextResponse("Bad Request(check proposal id again)", 400)
