from endpoints.classes import Resource

from .add_record import add_record
from .get_record import get_record

MONEY = [
    Resource(
        "GET",
        "/money",
        get_record,
        "Used for get money record",
        "Get money record",
    ),
    Resource(
        "POST",
        "/money",
        add_record,
        "Used for add new money record",
        "Add money record",
    ),
]
