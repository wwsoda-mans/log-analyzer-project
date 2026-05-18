from log_parser import parse_logs

logs=parse_logs("logs.txt")
for log in logs:
    log.show()
    print("-----")