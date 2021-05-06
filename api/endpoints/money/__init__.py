from endpoints.classes import Resource

from .post import post

MONEY = [
    Resource(
        "POST",
        "/money",
        post,
        "Used for add new money record",
        "Add money record",
    ),
]
