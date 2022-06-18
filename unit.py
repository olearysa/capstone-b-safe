import unittest
import main

class Testing(unittest.TestCase):
	self.math = main.Math() 
	def test_add(self):
		ans = self.math.add(2,2)
		self.assertEqual(ans,4)
	def test_minus(self):
		ans = self.math.minus(2,1)
		self.assertEqual(ans,1)
	def test_mult(self):
		ans = self.math.mult(2,2)
		self.assertEqual(ans,4)
	def test_div(self):
		ans = self.math.div(4,2)
		self.assertEqual(ans,2)

if __name__ == '__main__':
	unittest.main()
