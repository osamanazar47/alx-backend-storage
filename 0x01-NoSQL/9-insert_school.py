#!/usr/bin/env python3
""" Module for task 9 Insert a document"""


def insert_school(mongo_collection, **kwargs):
    """function that insrets a new doc"""
    result = mongo_collection.insert_one(kwargs)
    return result._id
