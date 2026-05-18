def count_by_level(logs):
    counts = {}

    for log in logs:
        if log.level in counts:
            counts[log.level] = counts[log.level] + 1
        else:
            counts[log.level] = 1

    return counts

def count_total_logs(logs):
    return len(logs)

def get_top_messages(logs, limit):
    message_counts = {}

    for log in logs:
        if log.message in message_counts:
            message_counts[log.message] = message_counts[log.message] + 1
        else:
            message_counts[log.message] = 1

    sorted_messages = sorted(message_counts.items(), key=lambda item: item[1], reverse=True)

    return sorted_messages[:limit]

def print_level_counts(counts):
    for level in counts:
        print(level + ":", counts[level])

def print_logs(logs):
    for log in logs:
        log.show()
        print("-----")