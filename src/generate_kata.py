from pathlib import Path
import os, re

signature_map = {
    "linear_search" : "def linear_search(haystack:list[int], needle:int) -> bool:",
    "binary_search" : "def binary_search(haystack:list[int], needle:int) -> bool:",
    "quick_sort" : "def quick_sort(arr: list[int]) :"
}

def generate_new_kata():
    days = count_days()
    folder_name = f"day{days+1}"
    src_dir = Path("src")/folder_name
    src_dir.mkdir(exist_ok=True)

    for kata_name, _ in signature_map.items():
        kata_file = src_dir / f"{kata_name}.py"
        with kata_file.open("w") as f:
            f.write(f"{signature_map[kata_name]}")
    init_file = src_dir / "__init__.py"
    with init_file.open("w") as f:
        f.write(f"# this is the __init__.py file for {folder_name}")

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
    

if __name__ == '__main__':
    generate_new_kata()

