import re
import importlib
import os
from types import ModuleType

def count_days():
    idx = 0
    def contains_day_patter(text: str):
        pattern = r'day\d+'
        if re.search(pattern, text):
            return True
        else :
            return False

    path = "./src"
    for _, dirs, _ in os.walk(path):
        for dir in dirs:
            if contains_day_patter(dir) :
                idx += 1
    return idx

def dynamic_import(kata_name: str) -> ModuleType :
    module_name = f"src.day{count_days()}.{kata_name}"
    module = importlib.import_module(module_name)
    return module