# David Chou
# Dylan Kogut
# Sean Dougherty
# Thomas Merod

# Market Data Simulator
# main.py

import csv # for reading csvs
import sys # for reading command line arguments
from TupleList import TupleList # for TupleLists
from Clock import Clock # for timing things

# Cmd Line Args checking
if not len(sys.argv) == 5:
	print("Correct syntax is: \"py(thon3) main.py filename processingRate(nanoseconds) runTime(nanoseconds) wantedBufferSize\"")
	print("Terminating...")
	sys.exit()

#Instance Variables (maybe not needed since TupleList exists?)

# Command Line Arg Instantiation
filename = sys.argv[1]  # First arg of command line must be filename of csv
processingRate = int(sys.argv[2])  # Second arg of command line must be processing rate in int (nanoseconds)
runTime = int(sys.argv[3])  # Arg of command line must be runtime in int (nanoseconds)
wantedBufferSize = int(sys.argv[4])  # Fourth arg of command line must be desired buffer size (just a number)

csvArray = TupleList()
csvArray.create(filename)



# # Main stuff here
# 	current_time = 0
# 	clock.start(); # Dylan

# # Build out our list of tuples ( time, packets_left ) - David

# # Create a while loop, where each loop simulates 1 second of operation

# 	while (current_time < desired_run_time)
# 		csvArray.getPacketLoad/TupleForCurrentTime() # David
# 		processingUnit.add_packet_load()
# 		processingUnit.processData()
# 		current_time += 1

# 	clock.end()
# 	clock.time_passed

# 	# Calculate Statistics - Thomas
# 		# timer
# 		# processingUnit
# 			# latency[]
# 			# throughput[]


# 	#print stats

# # This is where all the actual program goes!
print("Program output for filename: '" + filename + "'.") #since TupleList doesn't store filename
csvArray.print_tuple_list()