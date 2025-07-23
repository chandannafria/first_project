import logging
import os
from datetime import datetime

# Log file name with timestamp
log_file = f"log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
log_path = os.path.join("logs", log_file)
os.makedirs("logs", exist_ok=True)

log_file_path  = os.path.join(log_path , log_file)
# Configure logging
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s'
)

if __name__ =="__main__":
    logging.info("logging has statred")