#!/usr/bin/python3
"""6. Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """deserialized object from file"""
    with open(filename, "r", encoding="utf-8") as f:
        return (json.load(f))
