class Packet(object):


    def __init__(self, startTime, endTime):
        self.startTime = startTime
        self.endTime = endTime
        self.latency = 0

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime

    def getLatency(self):
        return self.endTime - self.startTime