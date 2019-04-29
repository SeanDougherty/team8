

class ProcessingUnit(object):

    def __init__(self, processing_rate, desired_max_buffer_size):
        self.packetBuffer = []
        self.packetsDone = []
        self.latency = []
        self.throughput = []
        self.maxBufferSize = desired_max_buffer_size
        self.actualMaxBufferSize = 0
        self.currentBufferSize = 0
        self.processingRate = processing_rate
        self.bufferSizeRunningTotal = []

    def get_packet_buffer(self):
        return self.packetBuffer

    def get_max_buffer_size(self):
        return self.actualMaxBufferSize

    def get_current_buffer_size(self):
        return self.currentBufferSize

    def calculate_buffer_size(self):
        if (self.currentBufferSize > self.actualMaxBufferSize):
            self.actualMaxBufferSize = self.currentBufferSize
        return self.currentBufferSize

    def get_packets_from_done_buffer(self):
        return self.packetsDone

    # Churns through packetBuffer for one simulated millisecond
    def process_data(self, ms_being_simulated):

        # Create a copy of the processing rate to keep track of how much "processing power" we have left
        processing_power = self.processingRate

        # Process packets in the packetBuffer until your processing power runs out or the packetBuffer is emptied
        while processing_power > 0:
            # If there are more packets in the next packetLoad than can be processed in this cycle,
            #   simply subtract the processing rate from your packetsLeft and update your metrics
            if self.packetBuffer[0][0] > processing_power:
                self.latency.append(ms_being_simulated - self.packetBuffer[0][1])
                self.throughput.append(processing_power)
                #print(self.packetBuffer[0]) #debugging
                packets_done_in_this_cycle = self.packetBuffer[0][0] - processing_power
                time_added_to_system = self.packetBuffer[0][1]
                self.packetsDone.append((packets_done_in_this_cycle, time_added_to_system))
                del self.packetBuffer[0]
                #print(self.packetBuffer[0]) #debugging
                processing_power = 0

            # Else if you have enough processing power to process the entire packet_load,
            #   remove that packet_load and update your metrics
            else:
                self.latency.append(ms_being_simulated - self.packetBuffer[0][1])
                self.throughput.append(self.packetBuffer[0][0])
                processing_power -= self.packetBuffer[0][0]
                del self.packetBuffer[0]


    def add_packets_from_input_list(self, ms_being_simulated, packets_to_process):
        packets_to_add = packets_to_process[ms_being_simulated]
        time_added_to_system = ms_being_simulated
        self.packetBuffer.append((packets_to_add, time_added_to_system))
        self.currentBufferSize += packets_to_add
        self.calculate_buffer_size()


    # Add any packets from the done buffer of the previous processing unit. We assume there is no transfer time and
    # that all 'processed' packets are able to be passed immediately to the next processing unit
    # in the chain.
    def add_packets_from_prior_proc_unit(self, proc_unit):
        packets_to_add_list = proc_unit.get_packets_from_done_buffer()
        for packets_to_add in packets_to_add_list:
            self.packetBuffer.append(packets_to_add)
            self.currentBufferSize += packets_to_add[0]
        self.calculate_buffer_size()
