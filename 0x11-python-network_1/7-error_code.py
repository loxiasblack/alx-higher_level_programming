#!/usr/bin/python3
"""send requests to the URL and display the body response
if the code_status is more than 400"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code > 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
