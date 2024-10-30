import functools
import signal
from typing import Any, Callable, Optional, ParamSpec, TypeVar

P = ParamSpec('P')
R = TypeVar('R')


class TimeoutException(Exception):
    """Custom exception for timeout"""
    pass


def timeout(seconds: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Decorator that adds a timeout to any function.

    Args:
        seconds (int): Maximum allowed execution time in seconds

    Returns:
        Callable: Decorated function that will raise TimeoutException if execution exceeds the timeout

    Example:
        @timeout(5)
        def slow_function():
            time.sleep(10)
            return "Done"
    """
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            def handler(signum: int, frame: Optional[Any]) -> None:
                raise TimeoutException(
                    f"Function '{func.__name__}' timed out after {seconds} seconds")

            # Set up the timeout handler
            original_handler = signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)

            try:
                result = func(*args, **kwargs)
            finally:
                # Restore the original handler and cancel the alarm
                signal.alarm(0)
                signal.signal(signal.SIGALRM, original_handler)

            return result
        return wrapper
    return decorator
