from models import Log

def parse_logs(filename):
    logs = []

    files=open(filename, "r")

    for line in files:
        line = line.strip()

        if line=="":
            continue

        parts=line.split(" ")

        if len(parts)<3:
            continue

        date = parts[0]
        level = parts[1]

        message = ""
        i=2

        while i<len(parts):
            message = message + parts[i] + " "
            i = i + 1

        message = message.strip()

        log=Log(date, level, message)

        logs.append(log)
    files.close()

    return logs