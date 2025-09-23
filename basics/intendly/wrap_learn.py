from functools import wraps
from typing import Callable, Any
import time


def expensive_function() -> None:
    '''expensive_function() docstring'''
    time.sleep(2)
    print("Done")


def main() -> None:
    expensive_function()

if __name__ == '__main__':
    main()