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
        
    #packet_load_array format [(3,0), (4,1), (6,2), (7,3)] packet_load, index (or timestamp)
    #processing_unit_array format [processing_unit_objects with processing rate and buffer size set]

def main(packet_load_array, processing_unit_array):

    #Instance Variables (maybe not needed since TupleList exists?)
    clock = Clock()
    clock.start_stop()

    is_program_done = False
    ms_being_simulated = 0 
    
    def check_is_program_done(desired_runtime_ms, ms_being_simulated, packets_to_process, current_proc_unit):
        program_done = True
        if ms_being_simulated+1 < desired_run_time_ms:
            program_done = False
        if ms_being_simulated+1 < len(packets_to_process):
            program_done = False
        if current_proc_unit.get_current_buffer_size() > 0:
            program_done = False
        return program_done


    # Create a while loop, where each loop simulates 1 millisecond of operation
    while is_program_done == False:
        for idx in range(num_of_proc_units):
            current_proc_unit = proc_unit_list[idx]
            if idx == 0:
                if ms_being_simulated < desired_run_time_ms:
                    #print("ms_being_simulated: " + str(ms_being_simulated))
                    current_proc_unit.add_packets_from_input_list(packets_to_process, ms_being_simulated)
                print("Current Processing Unit = " + str(idx))
                current_proc_unit.process_data(ms_being_simulated)
            else:
                print("Current Processing Unit = " + str(idx))
                current_proc_unit.process_data(ms_being_simulated)

            if idx + 1 < num_of_proc_units:
                #print("this is happening")
                next_proc_unit = proc_unit_list[idx+1]
                next_proc_unit.add_packets_from_prior_proc_unit(current_proc_unit)

            is_program_done = check_is_program_done(desired_run_time_ms, ms_being_simulated, packets_to_process, current_proc_unit)
        print("simulating: " + str(ms_being_simulated))
        ms_being_simulated += 1

    #lengthOfpacketBufferAtEnd = len(processingUnit.packetBuffer) #debugging
    #print(processingUnit.packetBuffer[lengthOfpacketBufferAtEnd - 1]) #debugging

    clock.start_stop()
    print("A " + str(desired_run_time_ms) + " second long simulation was completed in " + str(clock.elapsed) + " second(s).")
    
    #add return statement that will return the average latency that david is working on
