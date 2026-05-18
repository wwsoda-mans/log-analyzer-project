from log_parser import parse_logs
from filters import filter_errors
from utils import print_title

def test_parser():
    print_title("PARSER TEST")

    logs = parse_logs("logs.txt")
    if len(logs) > 0:
        print("parser test passed")
    else:
        print("parser test failed")


def test_filter():
    print_title("FILTER TEST")
    logs = parse_logs("logs.txt")
    errors = filter_errors(logs)
    if len(errors) > 0:
        print("filter test passed")
    else:
        print("filter test failed")
test_parser()
print()

test_filter()