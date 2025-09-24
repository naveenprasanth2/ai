from typing import Any, Dict

def singleton(cls):
    instances : Dict[Any , Any] = {}

    def get_instance(*args : Any, **kwargs : Any):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton
class Singleton:
    def __init__(self, value) -> None:
        self.value = value

if __name__ == '__main__':
    s1 = Singleton(30)
    s2 = Singleton(40)

    print(s1.value)  # Output: 30
    print(s2.value)  # Output: 30
    print(s1 is s2)  # Output: True