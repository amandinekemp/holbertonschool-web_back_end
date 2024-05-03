#!/usr/bin/env python3
"""Change all topics of a school document based on the name"""

def update_topics(mongo_collection, name, topics):
    """
    Args:
    mongo_collection (dictionary): The collection of documents to update
    name (string): The name of the school to update
    topics (list of strings): The list of topics approached in the school
    """
    mongo_collection.update_one({'name': name}, {'$set': {'topics': topics}})
