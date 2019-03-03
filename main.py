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

# Cmd Line Args checking
if not len(sys.argv) == 6:
	print("Correct syntax is: \"py(thon3) main.py filename processingRate(nanoseconds) runTime(nanoseconds) wantedBufferSize desiredRunTime(seconds)\"")
	print("Terminating...")
	sys.exit()



# Command Line Arg Instantiation
filename = sys.argv[1]  # First arg of command line must be filename of csv
processingRate = int(sys.argv[2])  # Second arg of command line must be processing rate in int (nanoseconds)
runTime = int(sys.argv[3])  # Arg of command line must be runtime in int (nanoseconds)
wantedBufferSize = int(sys.argv[4])  # Fourth arg of command line must be desired buffer size (just a number)
desired_run_time = int(sys.argv[5]) # Fifth arg of command line must be desired run time (in seconds)

#Instance Variables (maybe not needed since TupleList exists?)
processingUnit = ProcessingUnit(processingRate, wantedBufferSize)
clock = Clock()

# Main stuff here
current_time = 0
clock.start_stop() # Dylan

# Build out our list of tuples ( time, packets_left ) - David
csvArray = TupleList()
csvArray.create(filename)
# # Create a while loop, where each loop simulates 1 minute of operation

while (current_time < desired_run_time):
	processingUnit.add_to_buffer(csvArray.tuple_list[current_time][0], csvArray.tuple_list[current_time][1])
	for _ in range(60): #here's the simulation of churning data for 60 seconds!
		processingUnit.process_data(current_time * 60) #@Sean this is probably wrong maybe you want to fix this
	current_time += 1

clock.start_stop()
print(clock.elapsed)

	# Calculate Statistics - Thomas
		# timer
		# processingUnit
			# latency[]
			# throughput[]


	#print stats

print("Program output for filename: '" + filename + "'.") #since TupleList doesn't store filename
csvArray.print_tuple_list()
#print(csvArray.tuple_list[0][0])
#print(csvArray.tuple_list[:60])