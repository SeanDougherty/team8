import os

csv_file_name = input("What is the name of your .csv file? ")
#print(type(csv_file_name))
#print(csv_file_name)

processing_rate = input("Processing Rate (aka Packets Processed per Second: ")
#print(type(processing_rate))
#print(processing_rate)

desired_buffer_size = input("Desired Buffer Size: ")
#print(type(desired_buffer_size))
#print(desired_buffer_size)

desired_run_time_in_seconds = input("Desired Run Time (s): ")
#print(type(desired_run_time_in_seconds))
#print(desired_run_time_in_seconds)

csv_type = input("CSV Type: microseconds OR default: ")
#print(csv_type)

caller = "python3 main.py "+ csv_file_name+ " " + processing_rate+ " " + csv_type + " " + desired_buffer_size+ " " +desired_run_time_in_seconds
#print(caller)

os.system(caller)
