# David Chou's implementation of a Tuple List class
# Moved to a separate class by Dylan

import csv
import random
import math
import numpy as np, numpy.random

class TupleList:
    def __init__(self):
        self.rawCSV = []
        self.tuple_list = [] # Each index in this tuple list represents 1 minute of packets to process
        self.day = "Undefined"
        self.MICROSECOND_CONVERSION = 1000000
    
	#Used to fill the tuple_list with CSV contents to be used for processing
    def create(self, filename, csv_in_microseconds, desired_runtime_ms):
        with open(filename, "r") as f:
            reader = csv.reader(f)
            next(reader) # to get rid of the garbage header
            for row in reader:
                self.rawCSV.append(row[1])

            #print(self.rawCSV) #debugging
            #this shenanigans is to only read the day once so the program is faster
            #I didn't like changing the day every loop, that seems redundant and wasteful.

            row_count = len(self.rawCSV)

            if csv_in_microseconds:
                if row_count < desired_runtime_ms or desired_runtime_ms == 0:
                    desired_ms = row_count
                else:
                    desired_ms = desired_runtime_ms

            else:
                if row_count < desired_runtime_ms/(self.MICROSECOND_CONVERSION*60) or desired_runtime_ms == 0:
                    desired_ms = row_count*self.MICROSECOND_CONVERSION*60
                else:
                    desired_ms = desired_runtime_ms

            tuple_list = self.build_tuple_list(desired_ms, csv_in_microseconds, self.rawCSV)

            return tuple_list

    def build_tuple_list(self, desired_ms,csv_in_microseconds, rawCSV):
            tuple_list = []
            if csv_in_microseconds:
                for idx in range(desired_ms):
                    num_of_packets = rawCSV[idx]
                    print("num_of_packets = " + str(num_of_packets))
                    tuple_list.append((int(num_of_packets), idx))
            else:                
                current_row = 0  # The 0th row refers to the first row containing packet data in the csv
                packets_per_second = int(rawCSV[current_row])
                base_packets_per_microsecond = int(packets_per_second / self.MICROSECOND_CONVERSION)
                remainder_packets_per_microsecond = packets_per_second % self.MICROSECOND_CONVERSION
                packet_distribution = np.ones(self.MICROSECOND_CONVERSION)*base_packets_per_microsecond
                packet_distribution[0:remainder_packets_per_microsecond] += 1
                # trash = np.round_((np.random.dirichlet(np.ones(self.MICROSECOND_CONVERSION)*35, size=1) * packets_per_second)[0])
                #print(packet_distribution[:300])
                for idx in range(desired_ms):
                    if math.floor(idx/(self.MICROSECOND_CONVERSION*60)) > current_row:
                        current_row += 1
                        packets_per_second = rawCSV[current_row]
                        base_packets_per_microsecond = int(packets_per_second / self.MICROSECOND_CONVERSION)
                        remainder_packets_per_microsecond = packets_per_second % self.MICROSECOND_CONVERSION
                        packet_distribution = np.ones(self.MICROSECOND_CONVERSION)*base_packets_per_microsecond
                        packet_distribution[0:remainder_packets_per_microsecond] += 1
                        # trash = np.round_((np.random.dirichlet(np.ones(self.MICROSECOND_CONVERSION)*35, size=1)*packets_per_second)[0])
                        #print("packet_distribution = " + str(packet_distribution))
                    packets = packet_distribution[idx % self.MICROSECOND_CONVERSION]
                    #print(packets)
                    tuple_list.append((packets, idx))

            return tuple_list

    def print_tuple_list(self):
        #print("Program output for filename: '" + filename + "'.") #filename is not stored, unless we want it to be.
        print ("Date: " + self.day + ".")
        print(self.tuple_list)
