from log_parser import parse_log
from file_handler import filter_errors

from utils import print_title


def test_parser():
    logs = parse_log("logs.txt")

    if len(logs) > 0:
        print("parser test passed")
    else:
        print("parser test failed")
def test_filter():
    logs = parse_log("logs.txt")
    errors = filter_errors(logs)
    if isinstance(errors, list):
        print("filtering test passed")
    else:
        print("filtering test failed")
test_filter()
test_parser()