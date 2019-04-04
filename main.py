# David Chou
# Dylan Kogut
# Sean Dougherty
# Thomas Merod

# Market Data Simulator
# main.py

import csv # for reading csvs
import sys # for reading command line arguments
import math # for floor, ceil functions
from TupleList import TupleList # for TupleLists
from Clock import Clock # for timing things
from ProcessingUnit import ProcessingUnit # for processing units
from StatCalculator import StatCalculator
import random 

# Cmd Line Args checking
incorrectInput = False

if not len(sys.argv) == 5:
	print("Correct syntax is: \"py(thon3) main.py filename processingRate(milliseconds/packet) wantedBufferSize desiredRunTime(seconds)\"")
	print("Terminating...")
	sys.exit()

if float(sys.argv[2]) < 1:
	print("Processing Rate cannot be less than 1")
	incorrectInput = True

if int(sys.argv[3]) < 1:
	print("Desired Buffer Size cannot be less than 1")
	incorrectInput = True

if int(sys.argv[4]) < 1:
	print("Desired Run Time cannot be less than 1")
	incorrectInput = True

if incorrectInput:
	print("Incorrect input, terminating...")
	sys.exit()

# Command Line Arg Instantiation
filename = sys.argv[1]  # First arg of command line must be filename of csv
processingRate = float(sys.argv[2])  # Second arg of command line must be processing rate in int (milliseconds per packet)
wantedBufferSize = int(sys.argv[3])  # Third arg of command line must be desired buffer size (just a number)
desired_run_time = int(sys.argv[4]) # Fourth arg of command line must be desired run time (in seconds)

# Convert processing rate from milliseconds / 1 packet to packets / 1 millisecond
process_rate_packet_p_ms = 1 / processingRate

#Instance Variables (maybe not needed since TupleList exists?)
MILLISECONDS_PER_SECOND = 1000000
DISTRIB_MOD = 0.2
processingUnit = ProcessingUnit(process_rate_packet_p_ms, wantedBufferSize)
clock = Clock()

# Main stuff here
current_time = 0
clock.start_stop()

# Build out our list of tuples ( time, packets_left )
csvArray = TupleList()
csvArray.create(filename)
packetLoadsToProcess = csvArray.convert_tuple_list_to_seconds(DISTRIB_MOD)

# Poor attempt at limiting the runtime bug, needs rework
max_run_time = len(packetLoadsToProcess)
if (desired_run_time > max_run_time):
	desired_run_time = max_run_time

# Convert runtime from seconds to ms
desired_run_time_ms = desired_run_time * MILLISECONDS_PER_SECOND

# Create a while loop, where each loop simulates 1 millisecond of operation
while (current_time < desired_run_time):
	current_time_s = math.floor(current_time/1000)
	packet_load = packetLoadsToProcess[current_time_s]
	processingUnit.add_to_buffer(packet_load, current_time)
	processingUnit.process_data(current_time) # Process data for 1 millisecond
	current_time += 1

#lengthOfpacketBufferAtEnd = len(processingUnit.packetBuffer) #debugging
#print(processingUnit.packetBuffer[lengthOfpacketBufferAtEnd - 1]) #debugging

clock.start_stop()
print("A " + str(desired_run_time) + " second long simulation was completed in " + str(clock.elapsed) + " second(s).")

	# Calculate Statistics
		# timer
		# processingUnit
			# latency[]
			# throughput[]

	#avg latency
	#avg throughput
	#maxBufferSize

# print(sum(processingUnit.latency)/len(processingUnit.latency))
# print(sum(processingUnit.throughput)/len(processingUnit.throughput))

	#print stats
# print(processingUnit.currentBufferSize)
myStats = StatCalculator(processingUnit)
myStats.getStats()

# print("Program output for filename: '" + filename + "'.") #since TupleList doesn't store filename
# csvArray.print_tuple_list()
#print(csvArray.tuple_list[0][0])
#print(csvArray.tuple_list[:60])


# 12947080 - w/ a processing rate of 14k
# 11331280 - w/ a processing rate of 50k

