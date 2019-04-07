import unittest
from Clock import Clock

class TestClock(unittest.TestCase):
	
	def test_reset(self):
		self.assertEqual(Clock.reset(self), 0)
		
	
if __name__ == '__main__':
	unittest.main()