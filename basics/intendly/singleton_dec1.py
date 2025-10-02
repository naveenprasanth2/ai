from typing import Any, Dict, TypeVar, Type, cast

T = TypeVar('T')  # Generic type variable

def singleton(cls: Type[T]) -> Type[T]:
    instances : Dict[Type[T], T] = {}

    def get_instance(*args : Any, **kwargs : Any) -> T:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    # Use `cast` to tell the type checker that `get_instance` is of type `Type[T]`
    return cast(Type[T], get_instance)


@singleton
class Singleton:
    def __init__(self, value) -> None:
        self.value = value

if __name__ == '__main__':
    s1 : Singleton = Singleton(30)
    s2 : Singleton = Singleton(40)

    print(s1.value)  # Output: 30
    print(s2.value)  # Output: 30
    print(s1 is s2)  # Output: True