from typing import Optional, Any


class Singleton:
    _instance : Optional["Singleton"] = None

    def __new__(cls, *args : Any, **kwargs: Any) -> "Singleton":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, value : int = 0) -> None:
        if not hasattr(self, "_is_initialized"):
            self.value = value
            self._is_initialized = True


if __name__ == '__main__':
    s1 : Singleton = Singleton(30)
    s2 : Singleton = Singleton(40)


    print(s1.value)
    print(s2.value)