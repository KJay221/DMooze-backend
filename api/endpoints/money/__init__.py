from endpoints.classes import Resource

from .add_record import add_record

MONEY = [
    Resource(
        "POST",
        "/money",
        add_record,
        "Used for add new money record",
        "Add money record",
    ),
]
