#!/usr/bin/env python3
"""Module for task 0(writing strings to redis)"""
import redis
import uuid
from typing import Union, Callable, Any
import functools


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """initialization of the Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def count_calls(self, method: Callable) -> Callable:
        """Decorator to count how many times a method is called."""
        count = 0

        @functools.wraps(method)
        def wrapper(self, *args, **kwargs) -> Any:
            nonlocal count
            key = method.__qualname__
            count += 1
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Callable = None
            ) -> Union[str, bytes, int, float]:
        """Retrieve data from Redis and convert it using an optional callable function.

        Args:
            key: The key to retrieve the data.
            fn: A callable function to convert the data.

        Returns:
            The retrieved data, optionally converted using fn.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Retrieve data as a UTF-8 string.

        Args:
            key: The key to retrieve the data.

        Returns:
            The retrieved data as a string.
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Retrieve data as an integer.

        Args:
            key: The key to retrieve the data.

        Returns:
            The retrieved data as an integer.
        """
        return self.get(key, fn=int)
