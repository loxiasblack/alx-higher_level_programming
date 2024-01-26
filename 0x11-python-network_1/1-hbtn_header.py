#!/usr/bin/python3
"""scripts that diplay the id of the header"""

import sys
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        pass
    for key, value in response.headers.items():
        if key == "X-Request-Id":
            print(value)
