def filter_by_level(logs, level):
    filtered_logs = []

    for log in logs:
        if log.level == level:
            filtered_logs.append(log)

    return filtered_logs

def filter_by_date(logs, date):
    filtered_logs = []

    for log in logs:
        if log.date == date:
            filtered_logs.append(log)

    return filtered_logs

def filter_by_date_range(logs, start_date, end_date):
    filtered_logs = []

    for log in logs:
        if start_date <= log.date <= end_date:
            filtered_logs.append(log)

    return filtered_logs

def filter_by_message_word(logs, word):
    filtered_logs = []

    for log in logs:
        message = log.message.lower()
        search_word = word.lower()

        if search_word in message:
            filtered_logs.append(log)

    return filtered_logs

def filter_errors(logs):
    return [log for log in logs if "ERROR" in log]
