#!/usr/bin/env python3
"""Insert a document in Python"""
def insert_school(mongo_collection, **kwargs):
    """ a Python function that inserts a new document in a collection based on kwargs"""
    documents = mongo_collection.insert_one(kwargs)
    return documents.inserted_id
