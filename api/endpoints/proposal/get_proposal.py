from datetime import datetime, timedelta

from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from models import ImageList, MoneyList, Proposal

from .model import DBProposal, ProposalItem, ProposalReturn


def get_proposal(proposal_addr: str = "", page: int = -1):
    try:
        if page == -1:
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
                    "project_description": db_proposal.project_description.replace(
                        " ", ""
                    ),
                    "start_time": db_proposal.start_time,
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
        row_number = SESSION.query(Proposal).count()
        row_number = row_number - page * 9 + 1
        display_number = 9
        if row_number < 0:
            display_number = row_number + 8
            row_number = 1
        proposal_list = []
        for i in range(display_number):
            db_proposal = (
                SESSION.query(Proposal).filter(Proposal.id == row_number + i).first()
            )
            money_record = (
                SESSION.query(MoneyList)
                .filter(MoneyList.proposal_addr == db_proposal.proposal_addr)
                .all()
            )
            current_price = 0
            for money_item in money_record:
                current_price += money_item.money
            proposal_item = ProposalItem(
                **{
                    "project_name": db_proposal.project_name.replace(" ", ""),
                    "representative": db_proposal.representative.replace(" ", ""),
                    "img_url": SESSION.query(ImageList)
                    .filter(ImageList.proposal_addr == db_proposal.proposal_addr)
                    .first()
                    .image_url.replace(" ", ""),
                    "target_price": db_proposal.target_price,
                    "current_price": current_price,
                    "left_time": str(
                        timedelta(30) - (datetime.now() - db_proposal.start_time)
                    ),
                }
            )
            proposal_list.append(proposal_item)
        proposal_list.reverse()
        return proposal_list
    except Exception as error:
        logger.error(error)
        return PlainTextResponse("Bad Request or proposal_addr is wrong", 400)
