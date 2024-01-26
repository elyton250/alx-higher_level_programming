#!/usr/bin/python3
"""handlles error code"""
import urllib.request
import urllib.error
import sys
if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as resp:
            print(resp.read().decode("utf-8"))

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.status}")
