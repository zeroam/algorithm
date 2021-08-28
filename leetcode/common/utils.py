import logging
import time
from functools import wraps


def time_elpased(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        ret = func(*args, **kwargs)

        logging.info(f"[{func.__name__}] elapsed {(time.time() - start_time) * 1000:.2f} ms")

        return ret

    return wrapper
