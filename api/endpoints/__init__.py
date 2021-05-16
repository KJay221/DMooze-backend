"""Routing table, gather route to main router for API"""
from typing import List
from endpoints.classes import Resource

from .proposal import PROPOSAL
from .money import MONEY
from .image_list import IMAGE
from .withdrawal_list import WITHDRAWAL

RESOURCES: List[Resource] = PROPOSAL + MONEY + IMAGE + WITHDRAWAL
