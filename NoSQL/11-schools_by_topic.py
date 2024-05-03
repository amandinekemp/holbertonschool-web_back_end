#!/usr/bin/env python3
"""Returns the list of school having a specific topic"""

def schools_by_topic(mongo_collection, topic):
    """
    Args:
    mongo_collection (dictionary): The collection of documents to search
    topic (string): The topic to search for

    Returns:
    List: A list of schools that have the specified topic
    """
    schools = mongo_collection.find({'topics': topic})
    return [school for school in schools]
