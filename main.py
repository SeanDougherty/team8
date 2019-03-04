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

# Cmd Line Args checking
if not len(sys.argv) == 5:
	print("Correct syntax is: \"py(thon3) main.py filename processingRate(nanoseconds) wantedBufferSize desiredRunTime(seconds)\"")
	print("Terminating...")
	sys.exit()



# Command Line Arg Instantiation
filename = sys.argv[1]  # First arg of command line must be filename of csv
processingRate = int(sys.argv[2])  # Second arg of command line must be processing rate in int (packets per second)
# runTime = int(sys.argv[3])  # Arg of command line must be runtime in int (nanoseconds)
wantedBufferSize = int(sys.argv[3])  # Third arg of command line must be desired buffer size (just a number)
desired_run_time = int(sys.argv[4]) # Fourth arg of command line must be desired run time (in seconds)

#Instance Variables (maybe not needed since TupleList exists?)
processingUnit = ProcessingUnit(processingRate, wantedBufferSize)
clock = Clock()

# Main stuff here
current_time = 0
clock.start_stop() # Dylan

# Build out our list of tuples ( time, packets_left ) - David
csvArray = TupleList()
csvArray.create(filename)
packetLoadsToProcess = csvArray.convert_tuple_list_to_seconds()

maxRunTime = len(packetLoadsToProcess)
if (desired_run_time > maxRunTime):
	desired_run_time = maxRunTime

# Create a while loop, where each loop simulates 1 second of operation
while (current_time < desired_run_time):
	processingUnit.add_to_buffer(packetLoadsToProcess[current_time], current_time)
	processingUnit.process_data(current_time) # Process data for 1 second
	current_time += 1

#lengthOfpacketBufferAtEnd = len(processingUnit.packetBuffer) #debugging
#print(processingUnit.packetBuffer[lengthOfpacketBufferAtEnd - 1]) #debugging

clock.start_stop()
print("A " + str(desired_run_time) + " second long simulation was completed in " + str(clock.elapsed) + " second(s).")

	# Calculate Statistics - Thomas
		# timer
		# processingUnit
			# latency[]
			# throughput[]

	#avg latency
	#avg throughput
	#maxBufferSize

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

