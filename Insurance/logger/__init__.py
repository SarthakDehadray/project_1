import logging
from datetime import datetime
import os

#Creating logs directory to store log in files
LOG_DIR = "insurance_log"

#Creating file name for log file based on current timestamp
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

#Defining the path to store log with folder name
LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"

#Creating a log directory if it does not exist
os.makedirs(LOG_DIR,exist_ok = True)

# Creating file path for projects
LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)


logging.basicConfig(filename = LOG_FILE_PATH,filemode = "w",
                    level = logging.DEBUG,format = '[%(asctime)s %(name)s - %(levelname)s - %(message)s]') 