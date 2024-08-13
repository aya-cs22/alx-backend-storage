#!/usr/bin/env python3
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['logs']
collection = db['nginx']
# number of documents in this collection
total_logs = collection.count_documents({})
print(f"{total_logs} logs\n")
print("Methods:\n")
# number of documents with the method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    method_count = collection.count_documents({'method': method})
    print(f"\tmethod {'method'}: {method_count}")
status = collection.count_documents({'method': 'GET', 'path': '/status'})
print(f"{status} status check")
