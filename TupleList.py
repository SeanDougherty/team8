import csv

class TupleList(filename):
    def create():
        csvData = [] #this is the list of csv tuples
        with open(filename, "r") as f:
            reader = csv.reader(f)
            next(reader) # to get rid of the garbage header
            #this shenanigans is to only read the day once so the program is faster
            #I didn't like changing the day every loop, that seems redundant and wasteful.
            tempRow = next(reader)
            day = tempRow[0].strip().partition(' ')[0]
            tempTuple = (tempRow[1],tempRow[0].strip().partition(' ')[2])
            csvData.append(tempTuple)

            for row in reader:
                    if row[0][0].isdigit():
                            tempTuple = (row[1],row[0].strip().partition(' ')[2])
                            csvData.append(tempTuple)

            f.close()
