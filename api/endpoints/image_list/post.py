import os
from typing import List

import aiofiles
import pyimgur
from fastapi import File, UploadFile
from fastapi.responses import PlainTextResponse
from loguru import logger

from config import Config
from db import SESSION
from models import ImageList, Proposal


async def post(
    proposal_id: int,
    image_files: List[UploadFile] = File(...),
):
    try:
        db_proposal = (
            SESSION.query(Proposal).filter(Proposal.proposal_id == proposal_id).first()
        )
        if Config.IMGUR_CLIENT_ID == "NO_ID":
            return PlainTextResponse("Specify IMGUR_ID as environment variable.", 400)
        for image_object in enumerate(image_files):
            image_path = "./image.jpg"
            async with aiofiles.open(image_path, "wb") as image_file:
                image_data = await image_object[1].read()
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
        return PlainTextResponse("successfully create and update image info", 200)
    except Exception as error:
        logger.error(error)
        SESSION.rollback()
        return PlainTextResponse("Bad Request(check input image)", 400)
