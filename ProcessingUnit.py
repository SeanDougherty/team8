

class ProcessingUnit(object):

    def __init__(self, processing_rate, desired_max_buffer_size):
        self.packetBuffer = []
        self.latency = []
        self.throughput = []
        self.maxBufferSize = desired_max_buffer_size
        self.currentBufferSize = 0
        self.processingRate = processing_rate

    def get_packet_buffer(self):
        return self.packetBuffer

    def set_packet_buffer(self, packet_buffer):
        self.packetBuffer = packet_buffer
        self.calculate_buffer_size()

    def get_buffer_size(self):
        self.calculate_buffer_size()
        return self.currentBufferSize

    # Calculate current buffer size based off of array of packetLoad tuples and return value
    def calculate_buffer_size(self):
        self.currentBufferSize = 0
        for packetLoad in self.packetBuffer:
            self.currentBufferSize += packetLoad.PacketsLeft
        return self.currentBufferSize

    def add_to_buffer(self, packet_load):
        self.packetBuffer.append(packet_load)

    # Churns through packetBuffer for one simulated second
    def process_data(self, current_time):

        # Create a copy of the processing rate to keep track of how much "processing power" we have left
        processing_power = self.processingRate[:]

        # Process packets in the packetBuffer until your processing power runs out or the packetBuffer is emptied
        while processing_power > 0 and len(self.packetBuffer) > 0:

            # If there are more packets in the next packetLoad than can be processed in this cycle,
            #   simply subtract the processing rate from your packetsLeft and update your metrics
            if self.packetBuffer[0][1] > processing_power:
                self.latency.append(current_time - self.packetBuffer[0].StartTime)
                self.throughput.append(processing_power)
                processing_power = 0

            # Else if you have enough processing power to process the entire packet_load,
            #   remove that packet_load and update your metrics
            else:
                self.latency.append(current_time - self.packetBuffer[0].StartTime)
                self.throughput.append(self.packetBuffer[0].PacketsLeft)
                processing_power -= self.packetBuffer[0].PacketsLeft
                del self.packetBuffer[0]
