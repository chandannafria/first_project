import logging
import os
from datetime import datetime
from src.exception import CustomException

# Step 1: Create a logs directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Step 2: Create log file name (just the file, not a folder)
LOG_FILE = f"log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

# Step 3: Combine to form full path
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Step 4: Setup logger
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

from src.utils import save_object
def log_exception(e, error_detail):
    """
    Log the exception details.
    """
    logger.error(f"Exception occurred: {e}")
    logger.error(f"Error details: {error_detail}")
    raise CustomException(e, error_detail)