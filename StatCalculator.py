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
        self.buffer_size_list = ProcessingUnit.bufferSizeRunningTotal

    def drawGraph(self, statList, title, units):
        dataFrame = pd.DataFrame(np.array(statList))
        plt.figure(str(title))
        plt.plot(dataFrame.index, dataFrame)
        plt.title(title, fontsize = 14, fontweight = 'bold')
        plt.xlabel('seconds')
        plt.ylabel(units)
        lines = plt.plot(dataFrame)
        mplcursors.cursor(lines, hover = True)

    def drawBarChart(self, values, objects, title, units):
        plt.figure(str(title))         
        y_pos = np.arange(len(objects))
        plt.bar(y_pos, values, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel(units)
        plt.title(title)

    def getStats(self):
        pylab.ion()
        matplotlib.style.use('ggplot')

        self.latency.sort()
        latencies = [self.latency[int(len(self.latency)*.5)], self.latency[int(len(self.latency)*.75)], self.latency[int(len(self.latency)*.9)], self.latency[int(len(self.latency)*.99)], self.latency[int(len(self.latency)*.999)]]
        objects = ("P50", "P75", "P90", "P99", "P99.9")

        print("Max Buffer Size Was: ")
        print(int(self.max_buffer_size))
        print("Average Latency Was: ")
        print(str(self.average_latency) + " seconds")
        print("Average Throughput Was: ")
        print(str(self.average_throughput) + " packets/second")
        print("Visualization Showing Now")
        self.drawGraph(self.latency, 'Latency vs. Seconds', 'seconds')
        self.drawGraph(self.throughput, 'Throughput vs. seconds', 'packets/second')
        self.drawGraph(self.buffer_size_list, 'Buffer Size vs. Time', 'packets')
        self.drawBarChart(latencies, objects, "Latency Distribution", "seconds")
        plt.pause(1)
        input("Press Enter to End Simulation")