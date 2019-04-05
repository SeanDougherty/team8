from statistics import mean
from Clock import Clock
from ProcessingUnit import ProcessingUnit
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import pylab
import mplcursors

class StatCalculator(object):

    def __init__(self, ProcessingUnit):
        self.latency = ProcessingUnit.latency
        self.throughput = ProcessingUnit.throughput
        self.average_latency = mean(ProcessingUnit.latency)
        self.average_throughput = mean(ProcessingUnit.throughput)
        self.max_buffer_size = ProcessingUnit.get_actual_max_buffer_size()

    def drawGraph(self, statList, title, units):
        dataFrame = pd.DataFrame(np.array(statList))
        plt.figure(str(title))
        plt.plot(dataFrame.index, dataFrame)
        plt.title(title, fontsize = 14, fontweight = 'bold')
        plt.xlabel('seconds')
        plt.ylabel(units)
        lines = plt.plot(dataFrame)
        mplcursors.cursor(lines, hover = True)

    def getStats(self):
        pylab.ion()
        matplotlib.style.use('ggplot')
        print("Max Buffer Size Was: ")
        print(self.max_buffer_size)
        print("Average Latency Was: ")
        print(str(self.average_latency) + " milliseconds")
        print("Average Throughput Was: ")
        print(str(self.average_throughput) + " packets/millisecond")
        print("Visualization Showing Now")
        self.drawGraph(self.latency, 'Latency vs. Seconds', 'milliseconds')
        self.drawGraph(self.throughput, 'Throughput vs. Seconds', 'packets/millisecond')
        plt.pause(1)
        input("Press Enter to End Simulation")