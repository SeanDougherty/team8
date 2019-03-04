import math
from Clock import Clock
from ProcessingUnit import ProcessingUnit

class StatCalculator(object):

    def maxBufferSize():
        return(ProcessingUnit.get_actual_max_buffer_size())

    def latency():
        print("2")

    def throughput():
        print("3")  

    def getStats():
        print("Max Buffer Size Was: ")
        print(statCalculator.maxBufferSize())  
        print("Average Latency Was: ")
        print(statCalculator.latency())
        print("Average Throughput Was: ")
        print(statCalculator.throughput())
