#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB"""

# Import MongoClient from pymongo module
from pymongo import MongoClient


def log_stats():
    # Create a MongoClient to the running mongod instance
    client = MongoClient("mongodb://127.0.0.1:27017")
    # Access the 'logs' database and 'nginx' collection
    logs_collection = client.logs.nginx

    # Define the list of methods to check
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Count and print the total number of documents in the collection
    print(f"{logs_collection.count_documents({})} logs")

    # Print the count of each method type
    print("Methods:")
    for method in methods:
        # Count the number of documents with the current method
        count = logs_collection.count_documents({"method": method})
        # Print the method and its count
        print(f"\tmethod {method}: {count}")

    # Count the number of documents where method is'GET'and path is'/status'
    status_check_count = logs_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    # Print the count of status checks
    print(f"{status_check_count} status check")
