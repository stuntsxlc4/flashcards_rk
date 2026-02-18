import logging

from flashcards.example import add
from flashcards.logging_config import configure_logging

logger = logging.getLogger(__name__)


def main() -> None:
    """Logger."""
    configure_logging()
    logger.info("app  started")


if __name__ == "__main__":
    main()
    add(1, 2)

