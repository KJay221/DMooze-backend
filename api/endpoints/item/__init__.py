from endpoints.classes import Resource

from .create_item import create_item

ITEM = [
    Resource(
        "POST", "/item/create_item", create_item, "Used for create item", "Create item"
    ),
]
