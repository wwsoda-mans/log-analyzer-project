from log_parser import parse_logs
from analyzer import count_by_level, count_total_logs, get_top_messages, print_level_counts, print_logs
from filters import filter_by_level, filter_by_date, filter_by_message_word, filter_by_message_word, filter_by_level, \
    filter_errors, filter_by_date_range

logs = parse_logs("logs.txt")

print("ALL LOGS")
print_logs(logs)

print("TOTAL LOGS")
print(count_total_logs(logs))

print("COUNT BY LEVEL")
level_counts = count_by_level(logs)
print_level_counts(level_counts)

print("ERROR LOGS")
error_logs = filter_errors(logs)
print_logs(error_logs)

print("DATE RANGE LOGS")
date_logs = filter_by_date_range(logs, "2026-05-18", "2026-05-20")
print_logs(date_logs)

print("LOGS WITH WORD")
word_logs = filter_by_message_word(logs, "User")
print_logs(word_logs)

print("TOP MESSAGES")
top_messages = get_top_messages(logs, 3)
print(top_messages)
