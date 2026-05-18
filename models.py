
class Log:
    def __init__(self, date, level, message):
        self.date = date
        self.level = level
        self.message = message

    def show(self):
        print(self.date)
        print(self.level)
        print(self.message)