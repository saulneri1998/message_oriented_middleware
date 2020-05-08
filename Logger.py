from Singleton import Singleton
from datetime import datetime

@Singleton
class Logger:

    def __init__(self):
        self.logs = []

    def addLog(self, msg):
        timestamp = "[{}]".format(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
        self.logs.append(timestamp + " - "+ msg)

    def printLogs(self):
        for log in reversed(self.logs):
            print(log)