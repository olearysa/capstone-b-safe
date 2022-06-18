class Math: 
	def plus(self, a, b):
		return a+b
	def minus(self, a, b):
		return a-b
	def mult(self, a, b):
		return a*b
	def div(self, a, b):
		return a/b

if __name__ == '__main__':
	math = Math()
	print('2 plus 2 is ' + str(math.plus(2,2))
	print('2 minus 1 is ' + str(math.minus(2,1))
	print('2 times 2 is ' + str(math.mult(2,2))
	print('4 divided by 2 is ' + str(math.div(4,2))
