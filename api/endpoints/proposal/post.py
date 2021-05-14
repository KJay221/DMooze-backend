from datetime import datetime, timedelta

import pytz
from fastapi.responses import PlainTextResponse
from loguru import logger

from db import SESSION
from models import Proposal


def post():
    try:
        last_id = SESSION.query(Proposal).order_by(Proposal.proposal_id.desc()).first()
        if not last_id:
            last_id = 1
        else:
            last_id = last_id.proposal_id + 1
        new_proposal = Proposal(
            **{
                "proposal_id": last_id,
                "owner_addr": "",
                "target_price": 0,
                "project_description": "",
                "start_time": datetime.now(pytz.utc) + timedelta(hours=8),
                "project_name": "",
                "representative": "",
                "email": "",
                "phone": "",
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
