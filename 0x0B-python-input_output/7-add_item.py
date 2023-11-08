#!/usr/bin/python3

"""this module adds argument in a list"""


from sys import argv
import os

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
if not os.path.isfile(filename):
    with open(filename, 'w', encoding='utf-8') as n_file:
        n_file.write("[]")
json_list = []
try:
    json_list = load_from_json_file(filename)
except json.JSONDecoderError:
    pass
json_list.extend(argv[1:])
save_to_json_file(json_list, filename)
