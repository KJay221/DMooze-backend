from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from models import ImageList, Proposal

from .model import DBProposal, ProposalReturn


def get_proposal(proposal_id: int):
    try:
        db_proposal: DBProposal = (
            SESSION.query(Proposal).filter(Proposal.id == proposal_id).first()
        )
        proposal_return = ProposalReturn(
            **{
                "id": db_proposal.id,
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
            .filter(ImageList.proposal_id == db_proposal.id)
            .all()
        )
        for item in db_url:
            proposal_return.img_url.append(item.image_url.replace(" ", ""))
        return proposal_return
    except Exception as error:
        logger.error(error)
        return PlainTextResponse("Bad Request or id is wrong", 400)
