import unittest
from ProcessingUnit import ProcessingUnit

class TestProcessingUnit(unittest.TestCase):
    
    #Each test begins with creating a ProcessingUnit object with a processing rate of 100 and a desired buffer of at most 100
    def test_set_packet_buffer(self):
        c = ProcessingUnit(100,100)
        self.assertEqual(c.set_packet_buffer([(1,2)]), [(1,2)])
        
    def test_calculate_buffer_size(self):
        c = ProcessingUnit(100,100)
        #The buffer is instantiated as size 0 
        self.assertEqual(c.calculate_buffer_size(),0)
        #Test that it can calculate when the buffer is not empty
        c.set_packet_buffer([(1,2)]), [(1,2)]
        self.assertEqual(c.calculate_buffer_size(),1)
		
    def test_add_to_buffer(self):
        c = ProcessingUnit(100,100)
        c.set_packet_buffer([])
        self.assertEqual(c.add_to_buffer((3,4), 0), [(3,4)])
		
    def test_process_data(self):
        c = ProcessingUnit(100,100)
        self.assertEqual(c.set_packet_buffer([(1,2)]), [(1,2)])
        self.assertEqual(c.add_to_buffer((3,4), 0), [(1,2),(3,4)])
        #Examining the largest function in our program and all of its variables
        c.process_data(10)
		#Demonstrating that the packetBuffer list has been correctly "processed" or emptied
        self.assertEqual(c.packetBuffer, [])
        self.assertEqual(c.latency, [8,6])
        self.assertEqual(c.throughput, [1,3])
        self.assertEqual(c.latency, [8,6])
    
if __name__ == '__main__':
    unittest.main()

