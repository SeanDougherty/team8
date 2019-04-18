import os

csv_file_name = raw_input("What is the title of your input file? ")
#print(type(csv_file_name))
#print(csv_file_name)

processing_rate = raw_input("Processing Rate (aka Packets Processed per Second: ")
#print(type(processing_rate))
#print(processing_rate)

desired_buffer_size = raw_input("Desired Buffer Size: ")
#print(type(desired_buffer_size))
#print(desired_buffer_size)

desired_run_time_in_seconds = raw_input("Desired Run Time (s): ")
#print(type(desired_run_time_in_seconds))
#print(desired_run_time_in_seconds)

caller = "python3 main.py "+ csv_file_name+ " " + processing_rate+ " " +desired_buffer_size+ " " +desired_run_time_in_seconds
#print(caller)

os.system(caller)
