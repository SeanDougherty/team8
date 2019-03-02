# David Chou's implementation of a Tuple List class
# Moved to a separate class by Dylan

import csv

class TupleList:
    def __init__(self):
        self.tuple_list = []
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

    def print_tuple_list(self):
        #print("Program output for filename: '" + filename + "'.") #filename is not stored, unless we want it to be.
        print ("Date: " + self.day + ".")
        print(self.tuple_list)
