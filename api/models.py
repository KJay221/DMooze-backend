import json

from sqlalchemy import CHAR, INT, TIME, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from config import Config
from db import SESSION

BASE = declarative_base()


class Proposal(BASE):

    __tablename__ = "proposal"

    proposal_id = Column(INT, primary_key=True)
    owner_addr = Column(CHAR, nullable=False)
    target_price = Column(INT, nullable=False)
    project_description = Column(CHAR, nullable=False)
    start_time = Column(TIME, nullable=False)
    project_name = Column(CHAR, nullable=False)
    representative = Column(CHAR, nullable=False)
    email = Column(CHAR, nullable=False)
    phone = Column(CHAR, nullable=False)
    children_image_list = relationship("ImageList")


class ImageList(BASE):

    __tablename__ = "image_list"

    id = Column(INT, primary_key=True)
    image_url = Column(CHAR, nullable=False)
    proposal_id = Column(INT, ForeignKey("proposal.proposal_id"), nullable=False)


class MoneyList(BASE):

    __tablename__ = "money_list"

    id = Column(INT, primary_key=True)
    money = Column(INT, nullable=False)
    sponsor_addr = Column(CHAR, nullable=False)
    transaction_hash = Column(CHAR, nullable=False)
    proposal_id = Column(INT, ForeignKey("proposal.proposal_id"), nullable=False)


class WithdrawalList(BASE):

    __tablename__ = "withdrawal_list"

    id = Column(INT, primary_key=True)
    money = Column(INT, nullable=False)
    use_description = Column(CHAR, nullable=False)
    transaction_hash = Column(CHAR, nullable=False)
    proposal_id = Column(INT, ForeignKey("proposal.proposal_id"), nullable=False)


def init_db():
    if Config.FAKE_DATA_INSERT == "true":
        fake_data = json.load(open("fakedata.json"))
        for i, proposal_object in enumerate(fake_data):
            fake_proposal = Proposal(
                **{
                    "proposal_id": i + 1,
                    "owner_addr": proposal_object["owner_addr"],
                    "target_price": proposal_object["target_price"],
                    "project_description": proposal_object["project_description"],
                    "start_time": proposal_object["start_time"],
                    "project_name": proposal_object["project_name"],
                    "representative": proposal_object["representative"],
                    "email": proposal_object["email"],
                    "phone": proposal_object["phone"],
                }
            )
            SESSION.merge(fake_proposal)
            SESSION.commit()
            for j in range(len(proposal_object["image_url"])):
                last_id = SESSION.query(ImageList).order_by(ImageList.id.desc()).first()
                if not last_id:
                    last_id = 1
                else:
                    last_id = last_id.id + 1
                fake_imagelist = ImageList(
                    **{
                        "id": last_id,
                        "image_url": proposal_object["image_url"][j],
                        "proposal_id": i + 1,
                    }
                )
                SESSION.merge(fake_imagelist)
                SESSION.commit()
            for j in range(len(proposal_object["money_input"])):
                last_id = SESSION.query(MoneyList).order_by(MoneyList.id.desc()).first()
                if not last_id:
                    last_id = 1
                else:
                    last_id = last_id.id + 1
                fake_moneylist = MoneyList(
                    **{
                        "id": last_id,
                        "money": proposal_object["money_input"][j],
                        "proposal_id": i + 1,
                        "sponsor_addr": proposal_object["sponsor_addr"][j],
                        "transaction_hash": proposal_object["transaction_hash_input"][
                            j
                        ],
                    }
                )
                SESSION.merge(fake_moneylist)
                SESSION.commit()
            for j in range(len(proposal_object["money_output"])):
                last_id = (
                    SESSION.query(WithdrawalList)
                    .order_by(WithdrawalList.id.desc())
                    .first()
                )
                if not last_id:
                    last_id = 1
                else:
                    last_id = last_id.id + 1
                fake_withdrawal_list = WithdrawalList(
                    **{
                        "id": last_id,
                        "money": proposal_object["money_output"][j],
                        "proposal_id": i + 1,
                        "use_description": proposal_object["use_description"][j],
                        "transaction_hash": proposal_object["transaction_hash_output"][
                            j
                        ],
                    }
                )
                SESSION.merge(fake_withdrawal_list)
                SESSION.commit()
