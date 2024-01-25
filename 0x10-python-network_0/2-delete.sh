#!/bin/bash
# bash script that send delete request passed to the firest argument
curl -sX DELETE "$1"
