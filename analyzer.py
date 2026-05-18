def count_by_level(logs):
    level_counts = {}

    for log in logs:
        if log.level in level_counts:
            level_counts[log.level] = level_counts[log.level] + 1
        else:
            level_counts[log.level] = 1

    return level_counts

def count_total_logs(logs):
    return len(logs)

def get_top_messages(logs, limit):
    message_counts = {}

    for log in logs:
        message = log.message
        if message in message_counts:
            message_counts[message] = message_counts[message] + 1
        else:
            message_counts[message] = 1

    sorted_messages = sorted(message_counts.items(), key=lambda item: item[1], reverse=True)

    return sorted_messages[:limit]

def print_level_counts(level_counts):
    for level in level_counts:
        print(level + ":", level_counts[level])

def print_logs(logs):
    for log in logs:
        log.show()
        print("-----")

