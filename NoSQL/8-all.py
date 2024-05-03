#!/usr/bin/env python3
"""List all documents in a collection"""


from typing import List

def list_all(mongo_collection) -> List:
    """    
    Args:
    mongo_collection (dictionary): The collection of documents to list

    Returns:
    List: A list of all documents in the collection
    """
    documents = mongo_collection.find()
    return [doc for doc in documents]
