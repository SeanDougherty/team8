#David CHou
#Dylan Kogut
#Sean Dougherty
#Thomas Merod

#Market Data Simulator
#main.py

import csv #for reading csvs
import sys #for reading command line arguments

#Cmd Line Args checking
if not len(sys.argv) == 5:
	print("Correct syntax is: \"py(thon3) main.py filename processingRate(nanoseconds) runTime(nanoseconds) wantedBufferSize\"")
	print("Terminating...")
	sys.exit()

#Instance Variables
csvData = [] #this is the list of csv tuples
#packetBuffer = [] #this is the list that packet numbers go in
#timeStamp = [] # idk if we need this but if we do we have it!
day = "Undefined"

#Command Line Arg Instantiation
filename = sys.argv[1] # first arg of command line must be filename of csv
processingRate = int(sys.argv[2]) # second arg of command line must be processing rate in int (nanoseconds)
runTime = int(sys.argv[3]) #  arg of command line must be runtime in int (nanoseconds)
wantedBufferSize = int(sys.argv[4]) # fourth arg of command line must be desired buffer size (just a number)


#main stuff here

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

#This is where all the actual program goes!

print("Program output for filename: '" + filename + "'.")
print ("Date: " + day + ".")
print(csvData)