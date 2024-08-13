#!/usr/bin/env python3
"""Log stats module"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs.nginx

    total_logs = db.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = db.count_documents({'method': method})
        print(f"\tmethod {method}: {method_count}")
    status = db.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status} status check")
