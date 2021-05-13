from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from models import Proposal


async def delete(proposal_id: int):
    try:
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
