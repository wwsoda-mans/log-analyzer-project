def print_title(title):
    print("=" * 40)
    print(title)
    print("=" * 40)


def format_log(log):
    text = "[" + log.level + "]"
    text = text + log.message

    return text