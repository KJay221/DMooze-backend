from endpoints.classes import Resource

from .create_proposal import create_proposal
from .get_proposal import get_proposal

PROPOSAL = [
    Resource(
        "POST",
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
]
