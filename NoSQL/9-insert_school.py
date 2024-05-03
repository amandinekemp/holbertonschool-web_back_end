#!/usr/bin/env python3
"""Insert a new document in a collection based on kwargs"""

def insert_school(mongo_collection, **kwargs):
    """
    Args:
    mongo_collection (dictionary): The collection of documents to insert into
    **kwargs: The data to insert in the form of keyword arguments

    Returns:
    The new _id
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
