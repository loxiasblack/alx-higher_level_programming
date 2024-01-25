#!/bin/bash
# bash scripts that send request to diplay method on url
curl -si -X OPTIONS "$1" | grep Allow
