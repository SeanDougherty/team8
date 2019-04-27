import os

csv_file_name = raw_input("What is the name of your .csv file? ")
#print(type(csv_file_name))
#print(csv_file_name)

#processing_rate = raw_input("Processing Rate (aka Packets Processed per Second: ")
#print(type(processing_rate))
#print(processing_rate)

#desired_buffer_size = raw_input("Desired Buffer Size: ")
#print(type(desired_buffer_size))
#print(desired_buffer_size)

desired_run_time_in_seconds = raw_input("Desired Run Time (s): ")
#print(type(desired_run_time_in_seconds))
#print(desired_run_time_in_seconds)

csv_array_in_sec = raw_input("Is your csv aray in seconds? (0/1) ")

desired_processing_units = raw_input("Desired number of processing units: ")
desired_processing_units = int(desired_processing_units)
#print(type(desired_processing_units))
#print(desired_processing_units)

if desired_processing_units == 1:
    pu1_pr = raw_input("Desired processing rate for processing unit 1: ")
    pu1_bs = raw_input("Desired buffer size for processing unit 1: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs

if desired_processing_units == 2:
    pu1_pr = raw_input("Desired processing rate for processing unit 1: ")
    pu1_bs = raw_input("Desired buffer size for processing unit 1: ")
    pu2_pr = raw_input("Desired processing rate for processing unit 2: ")
    pu2_bs = raw_input("Desired buffer size for processing unit 2: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs + " " + pu2_pr + " " + pu2_bs

if desired_processing_units == 3:
    pu1_pr = raw_input("Desired processing rate for processing unit 1: ")
    pu1_bs = raw_input("Desired buffer size for processing unit 1: ")
    pu2_pr = raw_input("Desired processing rate for processing unit 2: ")
    pu2_bs = raw_input("Desired buffer size for processing unit 2: ")
    pu3_pr = raw_input("Desired processing rate for processing unit 3: ")
    pu3_bs = raw_input("Desired buffer size for processing unit 3: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs + " " + pu2_pr + " " + pu2_bs + " " + pu3_pr + " " + pu3_bs

if desired_processing_units == 4:
    pu1_pr = raw_input("Desired processing rate for processing unit 1: ")
    pu1_bs = raw_input("Desired buffer size for processing unit 1: ")
    pu2_pr = raw_input("Desired processing rate for processing unit 2: ")
    pu2_bs = raw_input("Desired buffer size for processing unit 2: ")
    pu3_pr = raw_input("Desired processing rate for processing unit 3: ")
    pu3_bs = raw_input("Desired buffer size for processing unit 3: ")
    pu4_pr = raw_input("Desired processing rate for processing unit 4: ")
    pu4_bs = raw_input("Desired buffer size for processing unit 4: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs + " " + pu2_pr + " " + pu2_bs + " " + pu3_pr + " " + pu3_bs + " " + pu4_pr + " " + pu4_bs

if desired_processing_units == 5:
    pu1_pr = raw_input("Desired processing rate for processing unit 1: ")
    pu1_bs = raw_input("Desired buffer size for processing unit 1: ")
    pu2_pr = raw_input("Desired processing rate for processing unit 2: ")
    pu2_bs = raw_input("Desired buffer size for processing unit 2: ")
    pu3_pr = raw_input("Desired processing rate for processing unit 3: ")
    pu3_bs = raw_input("Desired buffer size for processing unit 3: ")
    pu4_pr = raw_input("Desired processing rate for processing unit 4: ")
    pu4_bs = raw_input("Desired buffer size for processing unit 4: ")
    pu5_pr = raw_input("Desired processing rate for processing unit 5: ")
    pu5_bs = raw_input("Desired buffer size for processing unit 5: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs + " " + pu2_pr + " " + pu2_bs + " " + pu3_pr + " " + pu3_bs + " " + pu4_pr + " " + pu4_bs + " " + pu5_pr + " " + pu5_bs

if desired_processing_units == 6:
    pu1_pr = raw_input("Desired processing rate for processing unit 1: ")
    pu1_bs = raw_input("Desired buffer size for processing unit 1: ")
    pu2_pr = raw_input("Desired processing rate for processing unit 2: ")
    pu2_bs = raw_input("Desired buffer size for processing unit 2: ")
    pu3_pr = raw_input("Desired processing rate for processing unit 3: ")
    pu3_bs = raw_input("Desired buffer size for processing unit 3: ")
    pu4_pr = raw_input("Desired processing rate for processing unit 4: ")
    pu4_bs = raw_input("Desired buffer size for processing unit 4: ")
    pu5_pr = raw_input("Desired processing rate for processing unit 5: ")
    pu5_bs = raw_input("Desired buffer size for processing unit 5: ")
    pu6_pr = raw_input("Desired processing rate for processing unit 6: ")
    pu6_bs = raw_input("Desired buffer size for processing unit 6: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs + " " + pu2_pr + " " + pu2_bs + " " + pu3_pr + " " + pu3_bs + " " + pu4_pr + " " + pu4_bs + " " + pu5_pr + " " + pu5_bs + " " + pu6_pr + " " + pu6_bs

if desired_processing_units == 7:
    pu1_pr = raw_input("Desired processing rate for processing unit 1: ")
    pu1_bs = raw_input("Desired buffer size for processing unit 1: ")
    pu2_pr = raw_input("Desired processing rate for processing unit 2: ")
    pu2_bs = raw_input("Desired buffer size for processing unit 2: ")
    pu3_pr = raw_input("Desired processing rate for processing unit 3: ")
    pu3_bs = raw_input("Desired buffer size for processing unit 3: ")
    pu4_pr = raw_input("Desired processing rate for processing unit 4: ")
    pu4_bs = raw_input("Desired buffer size for processing unit 4: ")
    pu5_pr = raw_input("Desired processing rate for processing unit 5: ")
    pu5_bs = raw_input("Desired buffer size for processing unit 5: ")
    pu6_pr = raw_input("Desired processing rate for processing unit 6: ")
    pu6_bs = raw_input("Desired buffer size for processing unit 6: ")
    pu7_pr = raw_input("Desired processing rate for processing unit 7: ")
    pu7_bs = raw_input("Desired buffer size for processing unit 7: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs + " " + pu2_pr + " " + pu2_bs + " " + pu3_pr + " " + pu3_bs + " " + pu4_pr + " " + pu4_bs + " " + pu5_pr + " " + pu5_bs + " " + pu6_pr + " " + pu6_bs + " " + pu7_pr + " " + pu7_bs

if desired_processing_units == 8:
    pu1_pr = raw_input("Desired processing rate for processing unit 1: ")
    pu1_bs = raw_input("Desired buffer size for processing unit 1: ")
    pu2_pr = raw_input("Desired processing rate for processing unit 2: ")
    pu2_bs = raw_input("Desired buffer size for processing unit 2: ")
    pu3_pr = raw_input("Desired processing rate for processing unit 3: ")
    pu3_bs = raw_input("Desired buffer size for processing unit 3: ")
    pu4_pr = raw_input("Desired processing rate for processing unit 4: ")
    pu4_bs = raw_input("Desired buffer size for processing unit 4: ")
    pu5_pr = raw_input("Desired processing rate for processing unit 5: ")
    pu5_bs = raw_input("Desired buffer size for processing unit 5: ")
    pu6_pr = raw_input("Desired processing rate for processing unit 6: ")
    pu6_bs = raw_input("Desired buffer size for processing unit 6: ")
    pu7_pr = raw_input("Desired processing rate for processing unit 7: ")
    pu7_bs = raw_input("Desired buffer size for processing unit 7: ")
    pu8_pr = raw_input("Desired processing rate for processing unit 8: ")
    pu8_bs = raw_input("Desired buffer size for processing unit 8: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs + " " + pu2_pr + " " + pu2_bs + " " + pu3_pr + " " + pu3_bs + " " + pu4_pr + " " + pu4_bs + " " + pu5_pr + " " + pu5_bs + " " + pu6_pr + " " + pu6_bs + " " + pu7_pr + " " + pu7_bs + " " + pu8_pr + " " + pu8_bs

if desired_processing_units == 9:
    pu1_pr = raw_input("Desired processing rate for processing unit 1: ")
    pu1_bs = raw_input("Desired buffer size for processing unit 1: ")
    pu2_pr = raw_input("Desired processing rate for processing unit 2: ")
    pu2_bs = raw_input("Desired buffer size for processing unit 2: ")
    pu3_pr = raw_input("Desired processing rate for processing unit 3: ")
    pu3_bs = raw_input("Desired buffer size for processing unit 3: ")
    pu4_pr = raw_input("Desired processing rate for processing unit 4: ")
    pu4_bs = raw_input("Desired buffer size for processing unit 4: ")
    pu5_pr = raw_input("Desired processing rate for processing unit 5: ")
    pu5_bs = raw_input("Desired buffer size for processing unit 5: ")
    pu6_pr = raw_input("Desired processing rate for processing unit 6: ")
    pu6_bs = raw_input("Desired buffer size for processing unit 6: ")
    pu7_pr = raw_input("Desired processing rate for processing unit 7: ")
    pu7_bs = raw_input("Desired buffer size for processing unit 7: ")
    pu8_pr = raw_input("Desired processing rate for processing unit 8: ")
    pu8_bs = raw_input("Desired buffer size for processing unit 8: ")
    pu9_pr = raw_input("Desired processing rate for processing unit 9: ")
    pu9_bs = raw_input("Desired buffer size for processing unit 9: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs + " " + pu2_pr + " " + pu2_bs + " " + pu3_pr + " " + pu3_bs + " " + pu4_pr + " " + pu4_bs + " " + pu5_pr + " " + pu5_bs + " " + pu6_pr + " " + pu6_bs + " " + pu7_pr + " " + pu7_bs + " " + pu8_pr + " " + pu8_bs + " " + pu9_pr + " " + pu9_bs

if desired_processing_units == 10:
    pu1_pr = raw_input("Desired processing rate for processing unit 1: ")
    pu1_bs = raw_input("Desired buffer size for processing unit 1: ")
    pu2_pr = raw_input("Desired processing rate for processing unit 2: ")
    pu2_bs = raw_input("Desired buffer size for processing unit 2: ")
    pu3_pr = raw_input("Desired processing rate for processing unit 3: ")
    pu3_bs = raw_input("Desired buffer size for processing unit 3: ")
    pu4_pr = raw_input("Desired processing rate for processing unit 4: ")
    pu4_bs = raw_input("Desired buffer size for processing unit 4: ")
    pu5_pr = raw_input("Desired processing rate for processing unit 5: ")
    pu5_bs = raw_input("Desired buffer size for processing unit 5: ")
    pu6_pr = raw_input("Desired processing rate for processing unit 6: ")
    pu6_bs = raw_input("Desired buffer size for processing unit 6: ")
    pu7_pr = raw_input("Desired processing rate for processing unit 7: ")
    pu7_bs = raw_input("Desired buffer size for processing unit 7: ")
    pu8_pr = raw_input("Desired processing rate for processing unit 8: ")
    pu8_bs = raw_input("Desired buffer size for processing unit 8: ")
    pu9_pr = raw_input("Desired processing rate for processing unit 9: ")
    pu9_bs = raw_input("Desired buffer size for processing unit 9: ")
    pu10_pr = raw_input("Desired processing rate for processing unit 10: ")
    pu10_bs = raw_input("Desired buffer size for processing unit 10: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs + " " + pu2_pr + " " + pu2_bs + " " + pu3_pr + " " + pu3_bs + " " + pu4_pr + " " + pu4_bs + " " + pu5_pr + " " + pu5_bs + " " + pu6_pr + " " + pu6_bs + " " + pu7_pr + " " + pu7_bs + " " + pu8_pr + " " + pu8_bs + " " + pu9_pr + " " + pu9_bs + " " + pu10_pr + " " + pu10_bs + " "


print(caller)

#os.system(caller)
