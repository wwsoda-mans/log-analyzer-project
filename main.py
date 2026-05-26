from log_parser import parse_logs
from exporter import save_to_csv
logs=parse_logs("logs.txt")
for log in logs:
    log.show()
    print("-----")
save_to_csv(logs, "output.csv")

print("CSV file created")