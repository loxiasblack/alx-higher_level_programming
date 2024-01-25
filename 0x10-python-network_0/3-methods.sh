#!/bin/bash
# bash scripts that send request to diplay method on url
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
