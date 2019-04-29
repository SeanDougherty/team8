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
from ProcessingUnitFactory import ProcessingUnitFactory
from StatCalculator import StatCalculator
import random
import os

# Cmd Line Args checking
incorrectInput = False

# When arguments are missing that are required it will print a test example of how to correctly input data
if len(sys.argv) < 7:
	print("Correct syntax is: \"py(thon3) main.py filename desired_runtime csv_is_in_microseconds number_of_processing_units processing_rate_one buffer_size_one processing_rate_two....\"")
	print("Terminating...")
	sys.exit()

# If a filepath is not given it will assume there was a user input error
if not sys.argv[1]:
	print("File path may be incorrect")
	incorrectInput = True

# Will not accept Run Time that is less than 1
if float(sys.argv[2]) < float(0):
	print("Desired Run Time cannot be less than 0. Specifying a Run Time of 0 will cause the program to run until the entire CSV has been processed.")
	incorrectInput = True

if sys.argv[3] is not True and sys.argv[3] is not False:
	print("Expected boolean for whether or not csv is in milliseconds. Make sure your boolean is capitalized. (e.g.): False")
	incorrectInput = True

if float(sys.argv[4]) < float(1.0):
	print("number_of_processing_units should be a value between 1 and 10.")
	incorrectInput = True

for idx in range(sys.argv[4]):
	if float(sys.argv[idx+5]) <= float(0):
		print("Processing Rate cannot be less than 0")
		incorrectInput = True

	# Will not accept Buffer Size that is less than 1
	if float(sys.argv[idx+6]) < float(1.0):
		print("Desired Buffer Size cannot be less than 1")
		incorrectInput = True

# General shutdown message for incorrect inputs
if incorrectInput:
	print("Incorrect input, terminating...")
	sys.exit()

# Command Line Arg Instantiation
filename = sys.argv[1]  # First arg of command line must be filename of csv
desired_run_time_ms = float(sys.argv[2])  # Second arg of command line must be desired run time (in microseconds)
csv_is_microseconds = bool(sys.argv[3])  # Third arg of command line must be a boolean of whether or not the csv is given in microsecond format
num_of_proc_units = int(sys.argv[4])  # Fourth arg of command line must be an integer specifying the number of desired processing units

processing_unit_factory = ProcessingUnitFactory()
proc_unit_list = processing_unit_factory.build_processing_unit_list(sys, num_of_proc_units)

#Instance Variables (maybe not needed since TupleList exists?)
MILLISECONDS_PER_SECOND = 1000
DISTRIB_MOD = 0.05
clock = Clock()

# Main stuff here
current_time = 0
clock.start_stop()

# Build out our list of tuples ( time, packets_left )
csvArray = TupleList()
csvArray.create(filename,csv_is_microseconds,desired_run_time_ms)
packetLoadsToProcess = csvArray.convert_tuple_list_to_milliseconds(DISTRIB_MOD)
#print("csv shit is done")



is_program_done = False
ms_being_simulated = 0


# Create a while loop, where each loop simulates 1 millisecond of operation
while is_program_done == False:
	for idx in range(num_of_proc_units):
		# current_proc_unit = get_proc_unit_at_idx(proc_unit_list, idx)
		if idx == 0:
			current_proc_unit.add_packets_from_input_list(ms_being_simulated, packets_to_process)
			current_proc_unit.process_data()
		else:
			current_proc_unit.process_data()

		if idx + 1 < num_of_proc_units:
			# next_proc_unit = get_proc_unit_at_idx(proc_unit_list, idx+1)
			next_proc_unit.add_packets_from_prior_proc_unit(current_proc_unit)

		is_program_done = is_buffer_empty_and_input_list_empty(ms_being_simulated, packets_to_process, current_proc_unit)

	ms_being_simulated += 1

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
myStats = StatCalculator(processingUnittwo)
myStats.getStats()

# print("Program output for filename: '" + filename + "'.") #since TupleList doesn't store filename
# csvArray.print_tuple_list()
#print(csvArray.tuple_list[0][0])
#print(csvArray.tuple_list[:60])


# 12947080 - w/ a processing rate of 14k
# 11331280 - w/ a processing rate of 50k


