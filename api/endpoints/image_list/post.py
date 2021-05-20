import uuid
from typing import List

import aiofiles
from fastapi import File, UploadFile
from fastapi.responses import PlainTextResponse
from loguru import logger

from config import Config
from db import SESSION
from models import ImageList, Proposal


async def post(
    proposal_id: str,
    image_files: List[UploadFile] = File(...),
):
    try:
        db_proposal = (
            SESSION.query(Proposal).filter(Proposal.proposal_id == proposal_id).first()
        )
        for image_object in enumerate(image_files):
            img_uuid = str(uuid.uuid4())
            image_path = "./static/img/" + img_uuid + image_object[1].filename
            async with aiofiles.open(image_path, "wb") as image_file:
                image_data = await image_object[1].read()
                await image_file.write(image_data)
                image_path = (
                    Config().IMG_URL + "img/" + img_uuid + image_object[1].filename
                )
            new_img_url = ImageList(
                **{
                    "id": img_uuid,
                    "image_url": image_path,
                    "proposal_id": db_proposal.proposal_id,
                }
            )
            SESSION.add(new_img_url)
            SESSION.commit()
        return PlainTextResponse("successfully create and update image info", 200)
    except Exception as error:
        logger.error(error)
        SESSION.rollback()
        return PlainTextResponse("Bad Request(check input image or id is wrong)", 400)
