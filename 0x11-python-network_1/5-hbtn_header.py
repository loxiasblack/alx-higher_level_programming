#!/usr/bin/python3
"""diplay the value of the variable X-Request-Id in the response header"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    for key, value in r.headers.items():
        if key == "X-Request-Id":
            print(value)
