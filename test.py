import unittest
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Tests")
    parser.add_argument("-p", default="", help="Pattern for test file names")

    args = parser.parse_args()
    pattern = "*"+args.p+"*.py"

    print(pattern)

    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(start_dir="src/test", pattern=pattern)

    # for test_case in test_suite:
    #     print(f"{test_case}\n")
    #     for test in test_case._tests:
    #         print( f"{test}\n")

    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)