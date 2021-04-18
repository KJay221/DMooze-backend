from passlib.context import CryptContext
from sqlalchemy import BOOLEAN, CHAR, INT, VARCHAR, Column
from sqlalchemy.ext.declarative import declarative_base

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


def init_db():
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    manager_hashed_password = pwd_context.hash(Config.MANAGER_PASSWORD)

    if not SESSION.query(User).filter(User.account == "manager").first():
        SESSION.merge(User(**{"account": "manager",
                              "hashed_password": manager_hashed_password,
                              "money":10000,
                              "is_platform":True}))

    SESSION.merge(Fruit(**{"name": "apple", "count": 1}))
    SESSION.commit()
