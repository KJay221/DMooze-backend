import json

from sqlalchemy import CHAR, INT, TIME, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from db import SESSION

BASE = declarative_base()


class Proposal(BASE):

    __tablename__ = "proposal"

    proposal_id = Column(INT, primary_key=True)
    owner_addr = Column(CHAR, nullable=False)
    target_price = Column(INT, nullable=False)
    project_description = Column(CHAR)
    start_time = Column(TIME, nullable=False)
    project_name = Column(CHAR)
    representative = Column(CHAR)
    email = Column(CHAR)
    phone = Column(CHAR)
    children_image_list = relationship("ImageList")


class ImageList(BASE):

    __tablename__ = "image_list"

    id = Column(INT, primary_key=True)
    image_url = Column(CHAR)
    proposal_id = Column(INT, ForeignKey("proposal.proposal_id"), nullable=False)


class MoneyList(BASE):

    __tablename__ = "money_list"

    id = Column(INT, primary_key=True)
    money = Column(INT, nullable=False)
    proposal_id = Column(INT, ForeignKey("proposal.proposal_id"), nullable=False)


def init_db():
    SESSION.query(ImageList).delete()
    SESSION.query(MoneyList).delete()
    fake_data = json.load(open("fakedata.json"))
    for i in range(len(fake_data["proposal"])):
        fake_proposal = Proposal(
            **{
                "proposal_id": i + 1,
                "owner_addr": fake_data["proposal"][i]["owner_addr"],
                "target_price": fake_data["proposal"][i]["target_price"],
                "project_description": fake_data["proposal"][i]["project_description"],
                "start_time": fake_data["proposal"][i]["start_time"],
                "project_name": fake_data["proposal"][i]["project_name"],
                "representative": fake_data["proposal"][i]["representative"],
                "email": fake_data["proposal"][i]["email"],
                "phone": fake_data["proposal"][i]["phone"],
            }
        )
        SESSION.merge(fake_proposal)
        SESSION.commit()
        for j in range(len(fake_data["proposal"][i]["image_url"])):
            last_id = SESSION.query(ImageList).order_by(ImageList.id.desc()).first()
            if not last_id:
                last_id = 1
            else:
                last_id = last_id.id + 1
            fake_imagelist = ImageList(
                **{
                    "id": last_id,
                    "image_url": fake_data["proposal"][i]["image_url"][j],
                    "proposal_id": i + 1,
                }
            )
            SESSION.merge(fake_imagelist)
            SESSION.commit()
        for j in range(len(fake_data["proposal"][i]["money"])):
            last_id = SESSION.query(MoneyList).order_by(MoneyList.id.desc()).first()
            if not last_id:
                last_id = 1
            else:
                last_id = last_id.id + 1
            fake_moneylist = MoneyList(
                **{
                    "id": last_id,
                    "money": fake_data["proposal"][i]["money"][j],
                    "proposal_id": i + 1,
                }
            )
            SESSION.merge(fake_moneylist)
            SESSION.commit()
