# David Chou's implementation of a Tuple List class
# Moved to a separate class by Dylan

import csv

class TupleList:
    def __init__(self):
        self.tuple_list = [] # Each index in this tuple list represents 1 minute of packets to process
        self.day = "Undefined"
    
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

    def convert_tuple_list_to_seconds(self):
        seconds_tuple_list = [] # Each index in this tuple list represents 1 second of packets to process
        minute_counter = 0
        for tuple in self.tuple_list:
            for iterator in range(60):
                tuple[1] = minute_counter+iterator
                seconds_tuple_list.append(tuple)
            minute_counter += 60
        return seconds_tuple_list

    def print_tuple_list(self):
        #print("Program output for filename: '" + filename + "'.") #filename is not stored, unless we want it to be.
        print ("Date: " + self.day + ".")
        print(self.tuple_list)
