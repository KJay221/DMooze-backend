from datetime import datetime, timedelta
from typing import Optional

from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from models import ImageList, MoneyList, Proposal

from .model import DBProposal, ProposalItem


def get(useage: str, proposal_id: Optional[int] = None, page: Optional[int] = None):
    if useage == "get_proposal":
        return method_get_proposal(proposal_id=proposal_id, page=page)
    if useage == "get_page_number":
        return get_page_number()
    return PlainTextResponse("Bad Request Wrong useage", 400)


def method_get_proposal(proposal_id: int = None, page: int = None):
    try:
        if not page:
            print(proposal_id)
            db_proposal = (
                SESSION.query(Proposal)
                .filter(Proposal.proposal_id == proposal_id)
                .first()
            )
            return get_proposal_item(db_proposal)
        row_number = SESSION.query(Proposal).count()
        row_number = row_number - page * 9 + 1
        display_number = 9
        if row_number < 0:
            display_number = row_number + 8
            row_number = 1
        proposal_list = []
        for i in range(display_number):
            db_proposal = (
                SESSION.query(Proposal)
                .filter(Proposal.proposal_id == row_number + i)
                .first()
            )
            proposal_list.append(get_proposal_item(db_proposal))
        proposal_list.reverse()
        return proposal_list
    except Exception as error:
        logger.error(error)
        return PlainTextResponse("Bad Request or proposal_id is wrong", 400)


def get_page_number():
    try:
        row_number = SESSION.query(Proposal).count()
        page_number = row_number // 9 + 1
        return PlainTextResponse(str(page_number), 200)
    except Exception as error:
        logger.error(error)
        return PlainTextResponse("Bad Request", 400)


def get_proposal_item(db_proposal: DBProposal):
    money_record = (
        SESSION.query(MoneyList)
        .filter(MoneyList.proposal_id == db_proposal.proposal_id)
        .all()
    )
    current_price = 0
    for money_item in money_record:
        current_price += money_item.money
    proposal_item = ProposalItem(
        **{
            "proposal_id": db_proposal.proposal_id,
            "owner_addr": db_proposal.owner_addr.replace(" ", ""),
            "target_price": db_proposal.target_price,
            "current_price": current_price,
            "project_description": db_proposal.project_description.replace(" ", ""),
            "start_time": db_proposal.start_time,
            "left_time": str(timedelta(30) - (datetime.now() - db_proposal.start_time)),
            "project_name": db_proposal.project_name.replace(" ", ""),
            "representative": db_proposal.representative.replace(" ", ""),
            "email": db_proposal.email.replace(" ", ""),
            "phone": db_proposal.phone.replace(" ", ""),
            "img_url": [],
        }
    )
    db_img_list = (
        SESSION.query(ImageList)
        .filter(ImageList.proposal_id == db_proposal.proposal_id)
        .all()
    )
    for img_item in db_img_list:
        proposal_item.img_url.append(img_item.image_url.replace(" ", ""))
    return proposal_item
