#!/usr/bin/python3
"""
Loads an object from a text file containing JSON data.
"""
import json
import os.path
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = sys.argv[1:]

filename = "add_item.json"

if os.path.exists(filename):
    try:
        my_list = load_from_json_file(filename)
    except json.JSONDecodeError:
        my_list = []
else:
    my_list = []


my_list.extend(args)


save_to_json_file(my_list, filename)
