from src.logger import logging
from src.exception import CustomException
import sys

try:
    1 / 0
except Exception as e:
    logging.error("Exception occurred")
    raise CustomException(str(e), sys)
