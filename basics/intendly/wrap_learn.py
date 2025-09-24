from functools import wraps
from typing import Callable, Any
import time

def get_time(func : Callable) -> Callable:
    '''Gets the time of the given function'''
    return func

def expensive_function() -> None:
    '''expensive_function() docstring'''
    time.sleep(2)
    print("Done")


def main() -> None:
    expensive_function()

if __name__ == '__main__':
    main()