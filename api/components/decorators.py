from datetime import datetime

from api.components.logging import logger


def time_segment(func):
    def wrapper(*args, **kwargs):
        start = datetime.utcnow()

        response = func(*args, **kwargs)

        end = datetime.utcnow()
        delta = end - start

        logger.info(f"Function `{func.__name__}` operated for: {delta}")

        return response

    return wrapper