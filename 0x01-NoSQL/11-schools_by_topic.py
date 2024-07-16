#!/usr/bin/env python3
"""module for task 11 get schhols by a topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic passed ar an argument."""
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [document for document in mongo_collection.find(topic_filter)]
