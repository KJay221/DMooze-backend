from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from models import ImageList, Proposal

from .model import ProposalCreate


def create_proposal(create_proposal_input: ProposalCreate):
    try:
        new_proposal = Proposal(
            **{
                "proposal_addr": create_proposal_input.proposal_addr,
                "owner_addr": create_proposal_input.owner_addr,
                "target_price": create_proposal_input.target_price,
                "project_description": create_proposal_input.project_description,
                "start_time": create_proposal_input.start_time,
                "end_time": create_proposal_input.end_time,
                "project_name": create_proposal_input.project_name,
                "representative": create_proposal_input.representative,
                "email": create_proposal_input.email,
                "phone": create_proposal_input.phone,
            }
        )

        SESSION.add(new_proposal)
        SESSION.commit()
        SESSION.refresh(new_proposal)
        for image_url in create_proposal_input.img_url:
            new_img_url = ImageList(
                **{"image_url": image_url, "proposal_addr": new_proposal.proposal_addr}
            )
            SESSION.add(new_img_url)
            SESSION.commit()
        return PlainTextResponse("successfully create", 200)
    except Exception as error:
        logger.error(error)
        SESSION.rollback()
        return PlainTextResponse("Bad Request(check input data size and type)", 400)
