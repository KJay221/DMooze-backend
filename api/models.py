from sqlalchemy import CHAR, INT, TIME, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

BASE = declarative_base()


class Proposal(BASE):

    __tablename__ = "proposal"

    id = Column(INT, primary_key=True)
    proposal_addr = Column(CHAR, nullable=False, unique=True)
    owner_addr = Column(CHAR, nullable=False)
    target_price = Column(INT, nullable=False)
    project_description = Column(CHAR)
    start_time = Column(TIME, nullable=False)
    end_time = Column(TIME, nullable=False)
    project_name = Column(CHAR)
    representative = Column(CHAR)
    email = Column(CHAR)
    phone = Column(CHAR)
    children_image_list = relationship("ImageList")


class ImageList(BASE):

    __tablename__ = "image_list"

    id = Column(INT, primary_key=True)
    image_url = Column(CHAR)
    proposal_addr = Column(CHAR, ForeignKey('proposal.proposal_addr'), nullable=False)


class MoneyList(BASE):

    __tablename__ = "money_list"

    id = Column(INT, primary_key=True)
    money = Column(INT, nullable=False)
    proposal_addr = Column(CHAR, ForeignKey('proposal.proposal_addr'), nullable=False)


def init_db():
    pass
