#!/usr/bin/python3
"""this for dsplays a header content"""
import urllib.request
import sys
if __name__ == "__main__":
    """to prevent from working when imported"""
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader("X-Request-Id"))
