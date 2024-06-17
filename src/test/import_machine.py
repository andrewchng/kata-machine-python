import importlib
from src.generate_kata import count_days

def dynamic_import(kata_name: str):
    module_name = f"src.day{count_days()}.{kata_name}"
    module = importlib.import_module(module_name)
    return module
