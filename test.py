import unittest
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Tests")
    parser.add_argument("-p", default="*.py", help="Pattern for test file names")

    args = parser.parse_args()
    pattern = "*"+args.p+"*.py"

    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(start_dir="src/test", pattern=pattern)

    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)