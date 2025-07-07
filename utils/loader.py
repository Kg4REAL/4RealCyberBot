import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def load_json(filename):
    with open(os.path.join(BASE_DIR, "data", filename), "r", encoding="utf-8") as f:
        return json.load(f)

def load_text(filename):
    with open(os.path.join(BASE_DIR, "data", filename), "r", encoding="utf-8") as f:
        return f.read()
