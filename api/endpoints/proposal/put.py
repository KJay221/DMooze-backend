import os
from datetime import datetime
from typing import List

import aiofiles
import pyimgur
from fastapi import File, UploadFile
from fastapi.responses import PlainTextResponse
from loguru import logger

from config import Config
from db import SESSION
from models import ImageList, Proposal

from .model import ProposalCreate


async def put(
    create_proposal_input: ProposalCreate,
    proposal_id: int,
    image_files: List[UploadFile] = File(...),
):
    try:
        db_proposal = (
            SESSION.query(Proposal).filter(Proposal.proposal_id == proposal_id).first()
        )
        db_proposal.owner_addr = create_proposal_input.owner_addr
        db_proposal.target_price = create_proposal_input.target_price
        db_proposal.project_description = create_proposal_input.project_description
        db_proposal.start_time = datetime.now()
        db_proposal.project_name = create_proposal_input.project_name
        db_proposal.representative = create_proposal_input.representative
        db_proposal.email = create_proposal_input.email
        db_proposal.phone = create_proposal_input.phone
        SESSION.commit()
        if Config.IMGUR_CLIENT_ID == "NO_ID":
            return PlainTextResponse("Specify IMGUR_ID as environment variable.", 400)
        for image_object in enumerate(image_files):
            image_path = "./image.jpg"
            async with aiofiles.open(image_path, "wb") as image_file:
                image_data = await image_object.read()
                await image_file.write(image_data)
                image = pyimgur.Imgur(Config.IMGUR_CLIENT_ID)
                uploaded_image = image.upload_image(path=image_path)
                os.remove(image_path)
            last_id = SESSION.query(ImageList).order_by(ImageList.id.desc()).first()
            if not last_id:
                last_id = 1
            else:
                last_id = last_id.id + 1
            new_img_url = ImageList(
                **{
                    "id": last_id,
                    "image_url": uploaded_image.link,
                    "proposal_id": db_proposal.proposal_id,
                }
            )
            SESSION.add(new_img_url)
            SESSION.commit()
        return PlainTextResponse("successfully create and update info", 200)
    except Exception as error:
        logger.error(error)
        SESSION.rollback()
        return PlainTextResponse(
            "Bad Request(check input data size and type or id is wrong)", 400
        )
