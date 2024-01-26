#!/usr/bin/python3
""" script that takes your GitHub credentials
(username and password) and uses the GitHub API
to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    git_url = "https://api.github.com/user"
    creds = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get(git_url, auth=creds)
    print(req.json().get("id"))
