from models import Log

def parse_logs(filename):
    logs = []
    file=open(filename, "r")
    for line in file:
        line=line.strip()
        parts=line.split(" ")
        if len(parts)>3:
            date = parts[0]
            level = parts[1]
            message = ""
            i = 2
            while i<len(parts):
                message = message + parts[i]+""
                i = i+1
                log = log(date, level, message)

                logs.append(log)
            file.close()
            return logs
