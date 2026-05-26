import csv

def save_to_csv(logs, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "level", "message"])

        for log in logs:
            writer.writerow([
                log.date,
                log.level,
                log.message
            ])