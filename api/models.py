from sqlalchemy import CHAR, INT, TIME, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

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
    proposal_id = Column(INT, ForeignKey('proposal.proposal_id'), nullable=False)


class MoneyList(BASE):

    __tablename__ = "money_list"

    id = Column(INT, primary_key=True)
    money = Column(INT, nullable=False)
    proposal_id = Column(INT, ForeignKey('proposal.proposal_id'), nullable=False)


def init_db():
    pass
