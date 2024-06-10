import os
import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets')


def load_config(file_path):
    """ function to load json file """
    with open(os.path.join(ASSETS_DIR, file_path), 'r') as f:
        return json.load(f)
