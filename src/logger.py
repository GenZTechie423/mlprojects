import logging
import sys
import os
from datetime import datetime

project_root = os.path.abspath("C:/Users/sudhr/Downloads/mlprojects")
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.exceptions import CustomException
import sys

logs_path = os.path.join(os.getcwd(), "logs")
if not os.path.exists(logs_path):
    print(f"Creating directory: {logs_path}")
    os.makedirs(logs_path, exist_ok=True)

# Create a unique log file name using the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(
    os.getcwd(), "logs"
)  # Create a 'logs' directory in the current working directory


# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
print(f"Log file will be created at: {LOG_FILE_PATH}")

# Configure the logging system
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Timestamp|Line No.|Name|Level Name|Message
    level=logging.INFO,
)


# Also log to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)


# Test logging setup
logging.info("Logging setup complete.")


if __name__ == "__main__":
    print("Logging has started.")
    logging.info("Logging has started.")
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e, sys)
