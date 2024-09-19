import logging
from config import LOG_FILE

# Log for check data
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger(__name__)

def log_message(user_id, message):
    logger.info(f'User {user_id}: {message}')