# Redis Basic Operations

This project demonstrates basic usage of Redis in Python. It includes tasks related to creating a cache system, storing and retrieving data, counting method calls, and managing call history.

## Learning Objectives

- Learn how to use Redis for basic operations.
- Understand how to use Redis as a simple cache.

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- Code should adhere to the pycodestyle style (version 2.5).
- Modules, classes, and functions should have proper documentation.
- Functions and coroutines must be type-annotated.
## Resources

Refer to the following resources to enhance your understanding:

- [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)
- [Redis commands](https://redis.io/docs/latest/commands/)
- [Redis python client](https://redis-py.readthedocs.io/en/stable/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)

## Installation

### Install Redis on Ubuntu 18.04

```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
