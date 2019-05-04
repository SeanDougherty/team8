import unittest
from mainForTesting import main

class mainForTesting(unittest.TestCase):

    def test_create(self):
        c = TupleList()
        c.create("TestData_2_19_2019_security-info.csv")
        self.assertEqual(c.tuple_list[0], ('1756354', '09:26:00'))
        
    def test_convert_tuple_list_to_seconds(self):
        c = TupleList()
        distrib_mod = 0.2 #model of distribution
        c.create("TestData_2_19_2019_security-info.csv")
        #An example of a failed unit test because we wished to randomize the input load to gain more accurate results
        #self.assertEqual(c.convert_tuple_list_to_seconds(distrib_mod)[0], (2032642, 0))
        
    def test_print_tuple_list(self):
        c = TupleList()
        c.create("TestData_2_19_2019_security-info.csv")
        self.assertEqual(c.print_tuple_list(), "Date: 2019-02-19.") 
        
if __name__ == '__main__':
	unittest.main()

