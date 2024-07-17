#!/usr/bin/env python3
"""Module for task 0(writing strings to redis)"""
import redis
import uuid


class Cache:
    """Cache class"""
    def __init__(self):
        """initialization of the Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """takes a data argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
