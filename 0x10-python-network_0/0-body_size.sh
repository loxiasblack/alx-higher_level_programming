#!/bin/bash
# bash script that determine the size body
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
