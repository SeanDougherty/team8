from statistics import mean
from Clock import Clock
from ProcessingUnit import ProcessingUnit

class StatCalculator(object):

    def __init__(self, ProcessingUnit):
        self.average_latency = mean(ProcessingUnit.latency)
        self.average_throughput = mean(ProcessingUnit.throughput)
        self.max_buffer_size = ProcessingUnit.get_actual_max_buffer_size()

    def getStats(self):
        print("Max Buffer Size Was: ")
        print(self.max_buffer_size)
        print("Average Latency Was: ")
        print(str(self.average_latency) + " seconds")
        print("Average Throughput Was: ")
        print(str(self.average_throughput) + " packets/second")
