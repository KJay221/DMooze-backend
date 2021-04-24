"""Routing table, gather route to main router for API"""
from typing import List
from endpoints.classes import Resource

from .proposal import PROPOSAL
from .money import MONEY

RESOURCES: List[Resource] = PROPOSAL + MONEY
