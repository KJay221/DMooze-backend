from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from models import Proposal

from .model import DBProposal


def get_proposal(proposal_id: int):
    try:
        db_proposal: DBProposal = (
            SESSION.query(Proposal).filter(Proposal.id == proposal_id).first()
        )
        db_proposal.owner_addr = db_proposal.owner_addr.replace(" ", "")
        db_proposal.project_description = db_proposal.project_description.replace(
            " ", ""
        )
        db_proposal.project_name = db_proposal.project_name.replace(" ", "")
        db_proposal.representative = db_proposal.representative.replace(" ", "")
        db_proposal.email = db_proposal.email.replace(" ", "")
        db_proposal.phone = db_proposal.phone.replace(" ", "")
        return db_proposal
    except Exception as error:
        logger.error(error)
        return PlainTextResponse("Bad Request or id is wrong", 400)
