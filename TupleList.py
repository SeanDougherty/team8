# David Chou's implementation of a Tuple List class
# Moved to a separate class by Dylan

import csv
import random

class TupleList:
    def __init__(self):
        self.tuple_list = [] # Each index in this tuple list represents 1 minute of packets to process
        self.day = "Undefined"
    
	#Used to fill the tuple_list with CSV contents to be used for processing
    def create(self,filename):
        with open(filename, "r") as f:
            reader = csv.reader(f)
            next(reader) # to get rid of the garbage header
            #this shenanigans is to only read the day once so the program is faster
            #I didn't like changing the day every loop, that seems redundant and wasteful.
            tempRow = next(reader)
            self.day = tempRow[0].strip().partition(' ')[0]
            tempTuple = (tempRow[1],tempRow[0].strip().partition(' ')[2])
            self.tuple_list.append(tempTuple)

            for row in reader:
                    if row[0][0].isdigit():
                            tempTuple = (row[1],row[0].strip().partition(' ')[2])
                            self.tuple_list.append(tempTuple)

            f.close()

    def convert_tuple_list_to_seconds(self, distrib_mod):
        seconds_tuple_list = [] # Each index in this tuple list represents 1 second of packets to process
        minute_counter = 0
        for tuple in self.tuple_list:
            for iterator in range(60):
                load_size = float(tuple[0])
                packet_lower_bound = round(load_size - load_size * distrib_mod)
                packet_upper_bound = round(load_size + load_size * distrib_mod)
                randomized_load_size =  int(random.randint(packet_lower_bound, packet_upper_bound))
                tempTuple = (randomized_load_size, int(minute_counter+iterator))
                seconds_tuple_list.append(tempTuple)
            minute_counter += 60
        return seconds_tuple_list


    def print_tuple_list(self):
        #print("Program output for filename: '" + filename + "'.") #filename is not stored, unless we want it to be.
        print ("Date: " + self.day + ".")
        print(self.tuple_list)
