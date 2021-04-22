from endpoints.classes import Resource

from .create_proposal import create_proposal

PROPOSAL = [
    Resource(
        "POST",
        "/proposal/create_proposal",
        create_proposal,
        "Used for create proposal",
        "Create proposal",
    ),
]
