from functools import wraps
from typing import Any


def require_context(func):
    """Decorator to enforce context manager usage for methods"""
    @wraps(func)
    def wrapper(self, *args: Any, **kwargs: Any):
        if not self._in_context:
            raise RuntimeError(
                f"Method '{func.__name__}' can only be called within a context manager ('with' statement)"
            )
        return func(self, *args, **kwargs)
    return wrapper


class MyClass:
    def __init__(self, arg1: str):
        self.arg1 = arg1
        self._in_context = False

    def __enter__(self):
        self._in_context = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._in_context = False

    # This method can be called anytime
    def normal_method(self) -> str:
        return f"Normal method called with {self.arg1}"

    # This method requires context manager
    @require_context
    def protected_method(self) -> str:
        return f"Protected method called with {self.arg1}"


if __name__ == '__main__':
    obj = MyClass("test")
    print(obj.normal_method())  # Normal method called with test
    with obj as o:
        o.protected_method()
