#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Optional, Callable
class Cache():
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_uuid_key = str(uuid.uuid4())
        self._redis.set(random_uuid_key, data)
        # random_uuid = self._redis.get(random_uuid_key, data)
        return random_uuid_key

    def get(self, key: str, fn: Optional[Callable[[Union[str, bytes, int, float]], any]] = None) -> any:
        value = self._redis.get(key)
        if not (value):
            return None

        value = value.decode('utf-8')

        if fn is not None:
            return fn(value)
        
        return value
        
    def get_str(self, key: str) -> str:
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: int) -> int:
        return self.get(key lambda d: int(d))


