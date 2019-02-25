import time

class Buffer(object):


    def __init__(self):
        self.packetBuffer = {}
        self.bufferSize = 0
        self.startTime = time.time_ns()

    def getPacketBuffer(self):
        return self.packetBuffer

    def setPacketBuffer(self, packetBuffer):
        self.packetBuffer = packetBuffer
        self.bufferSize = len(packetBuffer)

    def getBufferSize(self):
        return self.bufferSize

    def calculateBufferSize(self):
        self.bufferSize = len(self.packetBuffer)

    def getStartTime(self):
        return self.startTime

    def buildPacketBuffer(self, csvString):
        # Need to look at the format we got from the fileReading methods in order to write this
        return

