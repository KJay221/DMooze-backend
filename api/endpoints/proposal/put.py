from datetime import datetime

from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from models import ImageList, Proposal

from .model import ProposalCreate


def put(create_proposal_input: ProposalCreate, success: bool, proposal_id: int):
    try:
        db_proposal = (
            SESSION.query(Proposal).filter(Proposal.proposal_id == proposal_id).first()
        )
        if success:
            db_proposal.owner_addr = create_proposal_input.owner_addr
            db_proposal.target_price = create_proposal_input.target_price
            db_proposal.project_description = create_proposal_input.project_description
            db_proposal.start_time = datetime.now()
            db_proposal.project_name = create_proposal_input.project_name
            db_proposal.representative = create_proposal_input.representative
            db_proposal.email = create_proposal_input.email
            db_proposal.phone = create_proposal_input.phone
            SESSION.commit()
            for image_url in create_proposal_input.img_url:
                new_img_url = ImageList(
                    **{"image_url": image_url, "proposal_id": db_proposal.proposal_id}
                )
                SESSION.add(new_img_url)
                SESSION.commit()
            return PlainTextResponse("successfully create and update info", 200)
        SESSION.delete(db_proposal)
        SESSION.commit()
        return PlainTextResponse("successfully receive fail msg", 200)
    except Exception as error:
        logger.error(error)
        SESSION.rollback()
        return PlainTextResponse(
            "Bad Request(check input data size and type or id is wrong)", 400
        )
