import json
import uuid

from sqlalchemy import CHAR, FLOAT, TIME, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from config import Config
from db import SESSION

BASE = declarative_base()


class Proposal(BASE):

    __tablename__ = "proposal"

    proposal_id = Column(CHAR, primary_key=True)
    owner_addr = Column(CHAR, nullable=False)
    target_price = Column(FLOAT, nullable=False)
    project_description = Column(CHAR, nullable=False)
    start_time = Column(TIME, nullable=False)
    project_name = Column(CHAR, nullable=False)
    representative = Column(CHAR, nullable=False)
    email = Column(CHAR, nullable=False)
    phone = Column(CHAR, nullable=False)
    create_hash = Column(CHAR, nullable=False)
    children_image_list = relationship("ImageList")


class ImageList(BASE):

    __tablename__ = "image_list"

    id = Column(CHAR, primary_key=True)
    image_url = Column(CHAR, nullable=False)
    proposal_id = Column(CHAR, ForeignKey("proposal.proposal_id"), nullable=False)


class MoneyList(BASE):

    __tablename__ = "money_list"

    id = Column(CHAR, primary_key=True)
    money = Column(FLOAT, nullable=False)
    sponsor_addr = Column(CHAR, nullable=False)
    transaction_hash = Column(CHAR, nullable=False)
    input_time = Column(TIME, nullable=False)
    proposal_id = Column(CHAR, ForeignKey("proposal.proposal_id"), nullable=False)


class WithdrawalList(BASE):

    __tablename__ = "withdrawal_list"

    id = Column(CHAR, primary_key=True)
    money = Column(FLOAT, nullable=False)
    use_description = Column(CHAR, nullable=False)
    transaction_hash = Column(CHAR, nullable=False)
    output_time = Column(TIME, nullable=False)
    proposal_id = Column(CHAR, ForeignKey("proposal.proposal_id"), nullable=False)


def init_db():
    if Config.FAKE_DATA_INSERT == "true":
        fake_data = json.load(open("fakedata.json"))
        for proposal_object in enumerate(fake_data):
            proposal_id = str(uuid.uuid4())
            fake_proposal = Proposal(
                **{
                    "proposal_id": proposal_id,
                    "owner_addr": proposal_object[1]["owner_addr"],
                    "target_price": proposal_object[1]["target_price"],
                    "project_description": proposal_object[1]["project_description"],
                    "start_time": proposal_object[1]["start_time"],
                    "project_name": proposal_object[1]["project_name"],
                    "representative": proposal_object[1]["representative"],
                    "email": proposal_object[1]["email"],
                    "phone": proposal_object[1]["phone"],
                    "create_hash": proposal_object[1]["create_hash"],
                }
            )
            SESSION.merge(fake_proposal)
            SESSION.commit()
            for j in range(len(proposal_object[1]["image_url"])):
                fake_imagelist = ImageList(
                    **{
                        "id": str(uuid.uuid4()),
                        "image_url": Config.IMG_URL
                        + "fakedata_img/"
                        + proposal_object[1]["image_url"][j],
                        "proposal_id": proposal_id,
                    }
                )
                SESSION.merge(fake_imagelist)
                SESSION.commit()
            for j in range(len(proposal_object[1]["money_input"])):
                fake_moneylist = MoneyList(
                    **{
                        "id": str(uuid.uuid4()),
                        "money": proposal_object[1]["money_input"][j],
                        "proposal_id": proposal_id,
                        "sponsor_addr": proposal_object[1]["sponsor_addr"][j],
                        "transaction_hash": proposal_object[1][
                            "transaction_hash_input"
                        ][j],
                        "input_time": proposal_object[1]["input_time"][j],
                    }
                )
                SESSION.merge(fake_moneylist)
                SESSION.commit()
            for j in range(len(proposal_object[1]["money_output"])):
                fake_withdrawal_list = WithdrawalList(
                    **{
                        "id": str(uuid.uuid4()),
                        "money": proposal_object[1]["money_output"][j],
                        "proposal_id": proposal_id,
                        "use_description": proposal_object[1]["use_description"][j],
                        "transaction_hash": proposal_object[1][
                            "transaction_hash_output"
                        ][j],
                        "output_time": proposal_object[1]["input_time"][j],
                    }
                )
                SESSION.merge(fake_withdrawal_list)
                SESSION.commit()
