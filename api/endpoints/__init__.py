"""Routing table, gather route to main router for API"""
from typing import List
from endpoints.classes import Resource

from .proposal import PROPOSAL

RESOURCES: List[Resource] = PROPOSAL
