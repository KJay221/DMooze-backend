from passlib.context import CryptContext
from sqlalchemy import BOOLEAN, CHAR, INT, TIME, VARCHAR, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from config import Config
from db import SESSION

BASE = declarative_base()


class Fruit(BASE):

    __tablename__ = "fruit"

    name = Column(VARCHAR, primary_key=True)
    count = Column(INT, nullable=False)

    def dumps(self):
        return {"name": self.name, "count": self.count}


class User(BASE):

    __tablename__ = "user"

    id = Column(INT, primary_key=True)
    account = Column(CHAR, unique=True)
    hashed_password = Column(CHAR)
    money = Column(INT)
    is_platform = Column(BOOLEAN, default=False)
    children = relationship("Item")


class Item(BASE):

    __tablename__ = "item"

    id = Column(INT, primary_key=True)
    owner_id = Column(INT, ForeignKey('user.id'), nullable=False)
    target_price = Column(INT, nullable=False)
    project_content = Column(CHAR)
    start_time = Column(TIME, nullable=False)
    end_time = Column(TIME, nullable=False)
    project_name = Column(CHAR)
    representative = Column(CHAR)
    email = Column(CHAR)
    phone = Column(CHAR)


class DonateRecord(BASE):

    __tablename__ = "donate_record"

    id = Column(INT, primary_key=True)
    project_id = Column(INT, ForeignKey('item.id'), nullable=False)
    donor_id = Column(INT, ForeignKey('user.id'), nullable=False)
    money = Column(INT)


class UseRecord(BASE):

    __tablename__ = "use_record"

    id = Column(INT, primary_key=True)
    project_id = Column(INT, ForeignKey('item.id'), nullable=False)
    money = Column(INT)
    purpose = Column(CHAR)


def init_db():
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    manager_hashed_password = pwd_context.hash(Config.MANAGER_PASSWORD)

    if not SESSION.query(User).filter(User.account == "manager").first():
        SESSION.merge(User(**{"account": "manager",
                              "hashed_password": manager_hashed_password,
                              "money": 10000,
                              "is_platform": True}))

    SESSION.merge(Fruit(**{"name": "apple", "count": 1}))
    SESSION.commit()
