import logging
import os

logging.basicConfig(
    filename="test.log",
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logging.info("Test log entry")
