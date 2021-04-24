from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from models import ImageList, Proposal

from .model import DBProposal, ProposalReturn


def get_proposal(proposal_addr: str = ""):
    try:
        db_proposal: DBProposal = (
            SESSION.query(Proposal)
            .filter(Proposal.proposal_addr == proposal_addr)
            .first()
        )
        proposal_return = ProposalReturn(
            **{
                "proposal_addr": db_proposal.proposal_addr,
                "owner_addr": db_proposal.owner_addr.replace(" ", ""),
                "target_price": db_proposal.target_price,
                "project_description": db_proposal.project_description.replace(" ", ""),
                "start_time": db_proposal.start_time,
                "end_time": db_proposal.end_time,
                "project_name": db_proposal.project_name.replace(" ", ""),
                "representative": db_proposal.representative.replace(" ", ""),
                "email": db_proposal.email.replace(" ", ""),
                "phone": db_proposal.phone.replace(" ", ""),
                "img_url": [],
            }
        )
        db_url = (
            SESSION.query(ImageList)
            .filter(ImageList.proposal_addr == db_proposal.proposal_addr)
            .all()
        )
        for item in db_url:
            proposal_return.img_url.append(item.image_url.replace(" ", ""))
        return proposal_return
    except Exception as error:
        logger.error(error)
        return PlainTextResponse("Bad Request or proposal_addr is wrong", 400)
