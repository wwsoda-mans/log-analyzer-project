def filter_by_level(logs, level):
    result = []

    for log in logs:
        if log.level == level:
            result.append(log)

    return result

def filter_by_date(logs, date):
    result = []

    for log in logs:
        if log.date == date:
            result.append(log)

    return result

def filter_by_message_word(logs, word):
    result = []

    for log in logs:
        if word.lower() in log.message.lower():
            result.append(log)

    return result
