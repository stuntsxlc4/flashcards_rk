import logging

from utils import log_around

logger = logging.getLogger(__name__)


@log_around
def add(a: int, b: int) -> int:
    """Add."""
    return a + b
