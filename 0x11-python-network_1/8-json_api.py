#!/usr/bin/python3
"""Sends a POST request with email as a parameter"""

import requests
import sys


if __name__ == "__main__":
    query_param = ""

    if len(sys.argv) > 1:
        query_param = sys.argv[1]

    r = requests.post("http://0.0.0.0:5000/search_user",
                      data={'q': sys.argv[1]})
    text = r.content.decode("utf-8")
    if not (text.startswith("{") and text.endswith("}\n")):
        print("Not a valid JSON")
    else:
        parts = text.strip("{'}\n").split(",")
        if not parts or len(parts) == 1 and parts[0] == "":
            print("No result")
        else:
            data = {}
            for part in parts:
                key, value = part.split(":")
                key = key.strip("'\"")
                value = value.strip("'\"")
                data[key] = value
            print("[{}] {}".format(data["id"], data["name"]))
