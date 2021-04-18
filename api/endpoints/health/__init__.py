from endpoints.classes import Resource

from .get import get

HEALTH = [Resource("GET", "/health", get, "Used for health check", "Health check")]
