import time
from typing import Callable


def wait_until(callback: Callable, error_msg: str = None, timeout=5, poll=0.5):
    start = time.time()
    while True:
        try:
            value = callback()
            if value:
                return value
        except Exception:
            time.sleep(poll)
        if time.time() - start > timeout:
            raise TimeoutError(error_msg)
        time.sleep(poll)
