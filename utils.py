import os
import json

from configurations import config


def get_property(value) -> object:
    return config.common_data[value]


def read_data():
    file_path = os.path.join(config.SCENARIO_DIR, "data.json")
    with open(file_path, "r") as json_file:
        data = json.loads(json_file.read())
    return data


# def read_data(file_name):
#     file_path = os.path.join(config.SCENARIO_DIR, file_name)
#     with open(file_path, "r") as json_file:
#         data = json.loads(json_file.read())
#     return data
#

def get_contacts_data():
    return os.listdir(config.SCENARIO_DIR)
