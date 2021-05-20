import uuid
from datetime import datetime, timedelta

import pytz
from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from models import Proposal


def post():
    try:
        new_proposal = Proposal(
            **{
                "proposal_id": str(uuid.uuid4()),
                "owner_addr": "",
                "target_price": 0,
                "project_description": "",
                "start_time": datetime.now(pytz.utc) + timedelta(hours=8),
                "project_name": "",
                "representative": "",
                "email": "",
                "phone": "",
                "create_hash": "",
            }
        )
        SESSION.add(new_proposal)
        SESSION.commit()
        SESSION.refresh(new_proposal)
        return new_proposal.proposal_id
    except Exception as error:
        logger.error(error)
        SESSION.rollback()
        return PlainTextResponse("Bad Request", 400)
