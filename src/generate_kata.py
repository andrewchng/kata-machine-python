from pathlib import Path

signature_map = {
    "linear_search" : "def linear_search(haystack:list, needle:int) -> bool:",
    "binary_search" : "def binary_search(haystack:list, needle:int) -> bool:"
}

def generate_new_kata():
    folder_name = "day1"
    src_dir = Path(folder_name)
    src_dir.mkdir(exist_ok=True)

    for kata_name, _ in signature_map.items():
        kata_file = src_dir / f"{kata_name}.py"
        with kata_file.open("w") as f:
            f.write(f"{signature_map[kata_name]}")
    init_file = src_dir / "__init__.py"
    with init_file.open("w") as f:
        f.write(f"# this is the __init__.py file for {folder_name}")

if __name__ == '__main__':
    generate_new_kata()