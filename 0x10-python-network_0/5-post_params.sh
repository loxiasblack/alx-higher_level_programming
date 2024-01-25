#!/bin/bash
#script that takes in a URL, sends a GET request to the URL,
curl -s -X POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
