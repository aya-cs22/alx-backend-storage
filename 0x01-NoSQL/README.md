# 0x01-NoSQL

## Overview

This project focuses on NoSQL databases, with an emphasis on MongoDB and its integration with Python. You'll explore the differences between SQL and NoSQL, learn about document storage, and practice querying, inserting, updating, and deleting data using MongoDB.

## Learning Objectives

By the end of this project, you should be able to:

- Understand what NoSQL means and how it differs from SQL.
- Explain the ACID properties and their relevance.
- Describe document storage and its benefits.
- Identify different types of NoSQL databases and their advantages.
- Query, insert, update, and delete information in a NoSQL database.
- Utilize MongoDB for managing NoSQL databases effectively.

## Resources

Refer to the following resources to enhance your understanding:

- [NoSQL Databases Explained](https://riak.com/resources/nosql-databases/)
- [What is NoSQL?](#)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=qUV2j3XBRHc)
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](https://www.youtube.com/watch?v=E-1xI85Zog8)
- [Aggregation](https://www.mongodb.com/docs/manual/aggregation/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [mongo Shell Methods](https://www.mongodb.com/docs/manual/reference/method/)
- [Mongosh](https://www.mongodb.com/docs/mongodb-shell/#mongodb-binary-bin.mongosh)

## Requirements

### MongoDB Command Files

- Your files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2).
- All files should end with a new line.
- The first line of all files should be a comment: `// my comment`.
- A `README.md` file at the root of the project folder is mandatory.
- File length will be tested using `wc`.

### Python Scripts

- Your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7) and PyMongo (version 3.10).
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code should adhere to `pycodestyle` version 2.5.*.
- File length will be tested using `wc`.
- All modules and functions should have documentation.
- Code should not execute when imported (use `if __name__ == "__main__":`).

## Installation

### MongoDB 4.2 on Ubuntu 18.04

Follow these steps to install MongoDB:

```bash
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
$ sudo service mongod status
$ mongo --version
MongoDB shell version v4.2.8
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'


---

Happy learning and exploring NoSQL databases!
```

You can customize the placeholders such as `<repository-url>` and `[your-email@example.com]` with your actual information.