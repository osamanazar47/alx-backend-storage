#!/usr/bin/env python3
"""A function that lists all documents in a collection"""
import pymongo


def list_all(mongo_collection):
    """returns a list of all documents"""
    return [document for document in mongo_collection.find()]
