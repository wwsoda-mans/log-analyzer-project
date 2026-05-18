def print_title(title):
    print("=" * 40)
    print(title)
    print("=" * 40)


def format_log(log):
    return f"[{log.leval}] {log.message}    "