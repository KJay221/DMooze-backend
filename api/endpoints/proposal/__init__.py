from endpoints.classes import Resource

from .create_proposal import create_proposal
from .get_id import get_id
from .get_page_number import get_page_number
from .get_proposal import get_proposal

PROPOSAL = [
    Resource(
        "POST",
        "/proposal/get_id",
        get_id,
        "Used for get id",
        "Get id",
    ),
    Resource(
        "PUT",
        "/proposal/create_proposal",
        create_proposal,
        "Used for create proposal",
        "Create proposal",
    ),
    Resource(
        "GET",
        "/proposal/get_proposal",
        get_proposal,
        "Used for get proposal by ID",
        "Get proposal",
    ),
    Resource(
        "GET",
        "/proposal/get_page_number",
        get_page_number,
        "Used for get page number",
        "Get page number",
    ),
]
