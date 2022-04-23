import logging
import os

LOG_LEVEL = int(os.environ.get("LOG_LEVEL", logging.INFO))
NAMESPACE = os.environ.get("NAMESPACE", "jibberator")

logger = logging.getLogger(NAMESPACE)
logger.setLevel(LOG_LEVEL)
