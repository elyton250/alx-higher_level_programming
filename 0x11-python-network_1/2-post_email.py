#!/usr/bin/python3
"""this posts email"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    """this is to prevent it to be imported"""
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': f'{email}'}
    data = urllib.parse.urlencode(values).encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
