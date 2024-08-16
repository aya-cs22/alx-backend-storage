#!/usr/bin/env python3
"""
a Cache class to store an instance of the Redis client as a private variable
named _redis (using redis.Redis())
a store method that takes a data argument and returns a string.
The method generates a random key (e.g. using uuid),
stores the input data in Redis using the random key and return the key.
"""

import redis
import uuid
from typing import Union, Callable, Any
import functools


def count_calls(method: Callable) -> Callable:
    qualname = method.__qualname__

    @functools.wraps(method)  # This preserves the original method's metadata
    def wrapper(self, *args, **kwargs):
        self._redis.incr(qualname)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    '''a decorator to store the history of inputs
    and outputs for a particular function.'''
    qualname = method.__qualname__
    input_key = qualname + ":inputs"
    output_key = qualname + ":outputs"

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper

def replay(self, method):
    '''display the history of calls of a particular function.'''
    qualname = method.__qualname__
    input_key = qualname + ":inputs"
    output_key = qualname + ":outputs"
    count = self.get(qualname).decode("utf-8")
    print(f"{qualname} was called {count} times:")

class Cache:
    '''store an instance of the Redis client'''
    def __init__(self):
        self._redis = redis.Redis()
        # resetting the db
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''generate a random key
        store the input data in Redis
        using the random key and return the key.'''
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        '''get data converted back to the desired format using the
        optional Callable'''
        data = self._redis.get(key)
        if fn:
            converted_data = fn(data)
            return converted_data
        return data

    def get_str(self, data: Any) -> str:
        '''convert data to string'''
        try:
            return str(data)
        except:
            return data

    def get_int(self, data: Any) -> int:
        '''convert data to integer'''
        try:
            return int(data)
        except:
            return data
        # #!/usr/bin/env python3
# import redis
# import uuid
# from typing import Union, Optional, Callable
# import functools

# def count_calls(method: Callable) -> Callable:
#     key = method.__qualname__
#     @functools.wraps(method)
#     def wrapper(self, *args, **kwargs):
#         self._redias.incr(key)
#         return method(self, *args, **kwargs)
#     return wrapper


# class Cache():
#     def __init__(self):
#         self._redis = redis.Redis()
#         self._redis.flushdb()

#     def store(self, data: Union[str, bytes, int, float]) -> str:
#         random_uuid_key = str(uuid.uuid4())
#         self._redis.set(random_uuid_key, data)
#         # random_uuid = self._redis.get(random_uuid_key, data)
#         return random_uuid_key

#     def get(self, key: str, fn: Optional[Callable[[Union[str, bytes, int, float]], any]] = None) -> any:
#         value = self._redis.get(key)
#         if not (value):
#             return None
#         # value = value.decode('utf-8')
#         if fn is not None:
#             return fn(value)
#         return value

#     def get_str(self, key: str) -> str:
#         return self.get(key, lambda d: d.decode('utf-8'))

#     def get_int(self, key: int) -> int:
#         return self.get(key, int)


