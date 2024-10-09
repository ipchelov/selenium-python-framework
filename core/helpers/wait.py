import time
from typing import Callable


def wait(
    condition: Callable[..., bool],
    error_message: str,
    timeout: int = 5,
    poll_frequency: float = 0.5,
) -> None:

    end_time = time.time() + timeout
    while time.time() < end_time:
        if condition():
            return None
        time.sleep(poll_frequency)

    raise TimeoutError(f"{error_message} after {timeout} seconds")
