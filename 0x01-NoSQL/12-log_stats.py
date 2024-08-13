#!/usr/bin/env python3
from pymongo import MongoClient
# client = MongoClient('mongodb://localhost:27017/')
# db = client['logs']
# collection = db['nginx']
if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs.nginx

    # number of documents in this collection
    # total_logs = collection.count_documents({})
    total_logs = db.count_documents({})
    print(f"{total_logs} logs\n")
    print("Methods:\n")
    # number of documents with the method
    # methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    # for method in methods:
    #     # method_count = collection.count_documents({'method': method})
    #     method_count = db.count_documents({'method': method})
    #     print(f"\tmethod {'method'}: {method_count}")
    get = db.count_documents({'method': 'GET'})
    post = db.count_documents({'method': 'POST'})
    put = db.count_documents({'method': 'PUT'})
    patch = db.count_documents({'method': 'PATCH'})
    delete = db.count_documents({'method': 'DELETE'})

    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    status = db.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status} status check")

