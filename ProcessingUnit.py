

class ProcessingUnit(object):

    def __init__(self, processing_rate, desired_max_buffer_size):
        self.packetBuffer = []
        self.latency = []
        self.throughput = []
        self.maxBufferSize = desired_max_buffer_size
        self.actualMaxBufferSize = 0
        self.currentBufferSize = 0
        self.processingRate = processing_rate
        self.bufferSizeRunningTotal = []

    # def __convert_to_packets_per_second(self,processing_rate_ns):
    #

    def get_packet_buffer(self):
        return self.packetBuffer

    def get_actual_max_buffer_size(self):
        return self.actualMaxBufferSize

    def set_packet_buffer(self, packet_buffer):
        self.packetBuffer = packet_buffer
        #self.calculate_buffer_size()

    def get_buffer_size(self):
        #self.calculate_buffer_size()
        return self.currentBufferSize



    def add_to_buffer(self, packet_load, current_time):
        self.packetBuffer.append(packet_load)
        self.currentBufferSize += packet_load[0]
        self.bufferSizeRunningTotal.append(self.currentBufferSize)
        if self.currentBufferSize > self.maxBufferSize:
            self.maxBufferSize = self.currentBufferSize
        #print(packet_load) #debugging

    # Churns through packetBuffer for one simulated microsecond
    def process_data(self, current_time):

        # Create a copy of the processing rate to keep track of how much "processing power" we have left
        processing_power = self.processingRate

        # Process packets in the packetBuffer until your processing power runs out or the packetBuffer is emptied
        while processing_power > 0 and len(self.packetBuffer) > 0:
            # If there are more packets in the next packetLoad than can be processed in this cycle,
            #   simply subtract the processing rate from your packetsLeft and update your metrics
            if self.packetBuffer[0][0] > processing_power:
                self.latency.append(current_time - self.packetBuffer[0][1])
                self.throughput.append(processing_power)
                self.currentBufferSize -= processing_power
                # print(self.packetBuffer[0]) #debugging
                tempPacketSize = self.packetBuffer[0][0] - processing_power
                tempSecondCount = self.packetBuffer[0][1]
                del self.packetBuffer[0]
                self.packetBuffer.insert(0, (tempPacketSize, tempSecondCount))
                # print(self.packetBuffer[0]) #debugging
                processing_power = 0

            # Else if you have enough processing power to process the entire packet_load,
            #   remove that packet_load and update your metrics
            else:
                self.latency.append(current_time - self.packetBuffer[0][1])
                self.throughput.append(self.packetBuffer[0][0])
                self.currentBufferSize -= self.packetBuffer[0][0]
                processing_power -= self.packetBuffer[0][0]
                del self.packetBuffer[0]
