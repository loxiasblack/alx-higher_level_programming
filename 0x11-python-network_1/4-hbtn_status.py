#!/usr/bin/python3
"""scripts that fetch with requests package"""

import requests

if __name__ == "__main__":

    s = requests.get("https://alx-intranet.hbtn.io/status")
    d = s.content.decode("utf-8")
    print("Body response:")
    print("\t- type: {}".format(type(d)))
    print("\t- content: {}".format(d))
