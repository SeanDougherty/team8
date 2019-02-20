#David CHou
#Dylan Kogut
#Sean Dougherty
#Thomas Merod

#Market Data Simulator
#main.py

import csv #for reading csvs
import sys #for reading command line arguments

#Instance Variables
packetBuffer = [] #this is the list that packet numbers go in
timeStamp = [] # idk if we need this but if we do we have it!
day = "Undefined"

#
filename = sys.argv[1] # first arg of command line must be filename of csv
#main stuff here

with open(filename, "r") as f:
	reader = csv.reader(f)
	next(reader) # to get rid of the garbage header
	#this shenanigans is to only read the day once so the program is faster
	#I didn't like changing the day every loop, that seems redundant and wasteful.
	tempRow = next(reader)
	day = tempRow[0].strip().partition(' ')[0]
	packetBuffer.append(tempRow[1])
	timeStamp.append(tempRow[0].strip().partition(' ')[2])
	for row in reader:
		if row[0][0].isdigit():
			packetBuffer.append(row[1])
			timeStamp.append(row[0].strip().partition(' ')[2])

	f.close()

#This is where all the actual program goes!

print("Program output for filename: '" + filename + "'.")
print ("Date: " + day + ".")
print(timeStamp)
print(packetBuffer)