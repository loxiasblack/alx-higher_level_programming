#!/usr/bin/python3
"""script that fetches the URL given and displayed the body"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        body = response.read()

    print("Body response:")
    print("     - type: {}".format(type(body)))
    print("     - content: {}".format(body))
    print("     - utf8 content: {}".format(body.decode('utf-8')))
