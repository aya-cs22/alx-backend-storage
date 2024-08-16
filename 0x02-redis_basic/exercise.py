#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Optional, Callable
import functools

def count_calls(method: Callable) -> Callable:
    key = method.__qualname__
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    key = method.__qualname__
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rupush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rupush(output_key, str(result))
        return result
    return wrapper

class Cache():
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_uuid_key = str(uuid.uuid4())
        self._redis.set(random_uuid_key, data)
        # random_uuid = self._redis.get(random_uuid_key, data)
        return random_uuid_key

    def get(self, key: str, fn: Optional[Callable[[Union[str, bytes, int, float]], any]] = None) -> any:
        value = self._redis.get(key)
        if not (value):
            return None
        # value = value.decode('utf-8')
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: int) -> int:
        return self.get(key, int)


