#!/usr/bin/python3
"""send POST request with a letter as a parameter"""

import requests
import sys

if __name__ == "__main__":
    if sys.argv[2] == None:
        sys.argv = ""
    payload = {'q': sys.argv[2]}
    r = requests.post(sys.argv[1], params=payload)
    print(r.text)
