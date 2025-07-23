import logging
import os
from datetime import datetime
import logging
import os
from datetime import datetime

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


# # Log file name with timestamp
# log_file = f"log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
# log_path = os.path.join(os.getcwd(),"logs", log_file)
# os.makedirs(log_path, exist_ok=True)

# log_file_path  = os.path.join(log_path , log_file)
# # Configure logging
# logging.basicConfig(
#     filename=log_file_path,
#     level=logging.INFO,
#     format='[%(asctime)s] %(levelname)s: %(message)s'
# )

# # logger = logging.getLogger(__name__)