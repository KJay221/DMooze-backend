from datetime import datetime, timedelta
from typing import Optional

import pytz
from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from models import ImageList, MoneyList, Proposal, WithdrawalList

from .model import DBProposal, ProposalItem


def get(
    usage: str,
    proposal_id: Optional[int] = None,
    page: Optional[int] = None,
    owner_addr: Optional[str] = None,
    expired: Optional[bool] = None,
):
    if usage == "get_proposal":
        return method_get_proposal(proposal_id=proposal_id, page=page, expired=expired)
    if usage == "get_page_number":
        return get_page_number(expired=expired)
    if usage == "get_owner_proposal":
        return get_owner_proposal(owner_addr=owner_addr)
    return PlainTextResponse("Bad Request Wrong usage", 400)


def method_get_proposal(
    proposal_id: int = None, page: int = None, expired: bool = None
):
    try:
        if not page:
            db_proposal = (
                SESSION.query(Proposal)
                .filter(Proposal.proposal_id == proposal_id)
                .first()
            )
            return get_proposal_item(db_proposal)
        db_proposal_list = None
        if expired:
            db_proposal_list = (
                SESSION.query(Proposal)
                .filter(Proposal.start_time < now_time() - timedelta(days=30))
                .all()
            )
        else:
            db_proposal_list = (
                SESSION.query(Proposal)
                .filter(Proposal.start_time > now_time() - timedelta(days=30))
                .all()
            )
        first_element_number = len(db_proposal_list) - (page - 1) * 9
        last_element_number = first_element_number - 9
        if last_element_number < 0:
            last_element_number = 0
        proposal_list = []
        for element in enumerate(
            db_proposal_list[last_element_number:first_element_number]
        ):
            db_proposal = (
                SESSION.query(Proposal)
                .filter(Proposal.proposal_id == element[1].proposal_id)
                .first()
            )
            proposal_list.append(get_proposal_item(db_proposal))
        proposal_list.reverse()
        return proposal_list
    except Exception as error:
        logger.error(error)
        return PlainTextResponse("Bad Request or proposal_id is wrong", 400)


def get_page_number(expired: bool):
    try:
        if expired:
            number_of_proposal = (
                SESSION.query(Proposal)
                .filter(Proposal.start_time < now_time() - timedelta(days=30))
                .count()
            )
            page_number = (number_of_proposal - 1) // 9 + 1
            return page_number
        number_of_proposal = (
            SESSION.query(Proposal)
            .filter(Proposal.start_time > now_time() - timedelta(days=30))
            .count()
        )
        page_number = (number_of_proposal - 1) // 9 + 1
        return page_number
    except Exception as error:
        logger.error(error)
        return PlainTextResponse("Bad Request", 400)


def get_owner_proposal(owner_addr: str):
    try:
        proposal_list = []
        for element in enumerate(
            SESSION.query(Proposal)
            .filter(Proposal.owner_addr == owner_addr)
            .order_by(Proposal.start_time.desc())
            .all()
        ):
            db_proposal = (
                SESSION.query(Proposal)
                .filter(Proposal.proposal_id == element[1].proposal_id)
                .first()
            )
            proposal_list.append(get_proposal_item(db_proposal))
        return proposal_list
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

    # time compute
    endtime_time = db_proposal.start_time + timedelta(days=30)
    left_time = (endtime_time - now_time()).days
    time_type = " 天"
    if left_time < 0:
        left_time = "expired"
        time_type = ""
    if left_time == 0:
        left_time = (endtime_time - now_time()).seconds // 3600
        time_type = " 小時"
    if left_time == 0:
        left_time = (endtime_time - now_time()).seconds // 60
        time_type = " 分鐘"
    if left_time == 0:
        left_time = (endtime_time - now_time()).seconds
        time_type = " 秒"
    proposal_item = ProposalItem(
        **{
            "proposal_id": db_proposal.proposal_id,
            "owner_addr": db_proposal.owner_addr.replace(" ", ""),
            "target_price": db_proposal.target_price,
            "current_price": current_price,
            "project_description": db_proposal.project_description.replace(" ", ""),
            "start_time": db_proposal.start_time,
            "left_time": str(left_time) + time_type,
            "project_name": db_proposal.project_name.replace(" ", ""),
            "representative": db_proposal.representative.replace(" ", ""),
            "email": db_proposal.email.replace(" ", ""),
            "phone": db_proposal.phone.replace(" ", ""),
            "create_hash": db_proposal.create_hash.replace(" ", ""),
            "img_url": [],
            "money_input": [],
            "sponsor_addr": [],
            "transaction_hash_input": [],
            "input_time": [],
            "money_output": [],
            "use_description": [],
            "transaction_hash_output": [],
            "output_time": [],
        }
    )
    db_data_list = (
        SESSION.query(ImageList)
        .filter(ImageList.proposal_id == db_proposal.proposal_id)
        .all()
    )
    for data_item in db_data_list:
        proposal_item.img_url.append(data_item.image_url.replace(" ", ""))
    db_data_list = (
        SESSION.query(MoneyList)
        .filter(MoneyList.proposal_id == db_proposal.proposal_id)
        .order_by(MoneyList.input_time.desc())
        .all()
    )
    for data_item in db_data_list:
        proposal_item.money_input.append(data_item.money)
        proposal_item.sponsor_addr.append(data_item.sponsor_addr.replace(" ", ""))
        proposal_item.transaction_hash_input.append(
            data_item.transaction_hash.replace(" ", "")
        )
        proposal_item.input_time.append(count_time(data_item.input_time))
    db_data_list = (
        SESSION.query(WithdrawalList)
        .filter(WithdrawalList.proposal_id == db_proposal.proposal_id)
        .order_by(WithdrawalList.output_time.desc())
        .all()
    )
    for data_item in db_data_list:
        proposal_item.money_output.append(data_item.money)
        proposal_item.use_description.append(data_item.use_description.replace(" ", ""))
        proposal_item.transaction_hash_output.append(
            data_item.transaction_hash.replace(" ", "")
        )
        proposal_item.output_time.append(count_time(data_item.output_time))
    return proposal_item


# time before
def count_time(start_time: datetime):
    left_time = (now_time() - start_time).days
    time_type = "天前"
    if left_time == 0:
        left_time = (now_time() - start_time).seconds // 3600
        time_type = "小時前"
    if left_time == 0:
        left_time = (now_time() - start_time).seconds // 60
        time_type = "分鐘前"
    if left_time == 0:
        return "剛剛"
    return str(left_time) + time_type


# get tw now time
def now_time():
    now = datetime.now(pytz.utc) + timedelta(hours=8)
    return datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
