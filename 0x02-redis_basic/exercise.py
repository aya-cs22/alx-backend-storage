#!/usr/bin/env python3
import redis
import uuid
from typing import Union
class Cache:
    def __init__(self, redis):
        self._redis = redis
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]):
        random_uuid = uuid.uuid4()
        self._redis.set(random_uuid)
        random_uuid = self._redis.get(random_uuid)
        return random_uuid
