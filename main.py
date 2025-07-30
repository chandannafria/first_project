from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
import os
import dill
import sys


try:
    a = 1 / 0
except Exception as e:
    raise CustomException(str(e), sys)
