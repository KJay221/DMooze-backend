from dataclasses import dataclass
from typing import Callable


@dataclass
class Resource:
    """Default resource for route"""

    method: str
    route: str
    endpoint: Callable
    description: str = "None"
    summary: str = "None"
