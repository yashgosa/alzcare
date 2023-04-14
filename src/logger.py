import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok = True)

LOG_FILE = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE,
    format= "[ %(asctime)s ] %(lineno)d %(levelname)s %(name)s %(message)s",
    level = logging.INFO
)
