import logging
from pathlib import Path


log_directory = Path(__file__).parent / "logs"
log_directory.mkdir(exist_ok=True)

logging.basicConfig(
    filename=log_directory / "etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)