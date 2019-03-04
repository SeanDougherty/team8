import datetime

class PacketLoad(list):
	
	#Object contains our StartTime upon load and keeps track of PacketsLeft to load from our Tuple array
    def __init__(self):
        self.StartTime = datetime.datetime.utcnow()
        self.PacketsLeft = count(list)
	#Distributes a single packet to be processed
    def feed(self):
        self.PacketsLeft - 1
	#Getter for StartTime at creation of PacketLoad
	def getStartTime(self):
		print (self.StartTime)
	#Getter for PacketsLeft in current PacketLoad
	def getPacketsLeft(self):
		print (self.getPacketsLeft)
