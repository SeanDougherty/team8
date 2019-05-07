import unittest
from mainForTesting import main
from ProcessingUnit import ProcessingUnit
from ProcessingUnitFactory import ProcessingUnitFactory

class mainForTesting(unittest.TestCase):
      
        #IR > PUR
    def test_IR_greater(self):
        packets_to_process = [(3,0), (4,1), (6,2), (7,3)] #packet load array input
        sys_vector = [0,0,4,0,1,3,100] #processing unit(s) input
        d = main(packets_to_process, sys_vector)
        self.assertEqual(d, "1.0")
        
        #IR < PUR
    def test_IR_less(self):
        packets_to_process = [(3,0), (4,1), (6,2), (7,3)] #packet load array input
        sys_vector = [0,0,4,0,1,5,100] #processing unit(s) input
        d = main(packets_to_process, sys_vector)
        self.assertEqual(d, "0.2")
        
        #IR == PUR
    def test_IR_Equal(self):
        packets_to_process = [(5,0), (5,1), (5,2), (5,3)] #packet load array input
        sys_vector = [0,0,4,0,1,4,100] #processing unit(s) input
        d = main(packets_to_process, sys_vector)
        self.assertEqual(d, "0.5")
        
        #IR increasing 5 -> 10 -> 15
    def test_IR_INC(self):
        packets_to_process = [(3,0), (4,1), (6,2), (7,3)] #packet load array input
        sys_vector = [0,0,4,0,1,4,100] #processing unit(s) input
        d = main(packets_to_process, sys_vector)
        self.assertEqual(d, "0.4")
        
        #IR decreasing 15 -> 10 -> 5 
    def test_IR_DEC(self):
        packets_to_process = [(7,0), (6,1), (4,2), (3,3)] #packet load array input
        sys_vector = [0,0,4,0,1,4,100] #processing unit(s) input
        d = main(packets_to_process, sys_vector)
        self.assertEqual(d, "0.85")
        
if __name__ == '__main__':
	unittest.main()

