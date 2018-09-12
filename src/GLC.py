

class  GeneradorCongruencialLineal(object) :
	
	def __init__(self, multiplier, increment, module):
		self.multiplier = multiplier
		self.increment = increment
		self.module = module

	def __init__ (self):
		self.multiplier = 1013904223
		self.increment = 1664525
		self.module = 2**32

	def generate_random(self,seed):
		return (self.multiplier*seed+self.increment)%self.module

	def generate_random_padron(self):
		padrones=int(96604+79478+84906 /3)
		return (self.multiplier*padrones+self.increment)%self.module

	def _generate_n_random_numbers(self,seed,n,number_list):
		for x in range(0,n):
			new_number= (self.multiplier*seed+self.increment)%self.module
			number_list.append(new_number)
			seed=new_number
		return number_list

	def generate_n_random_numbers(self,seed,n):
		number_list=[]
		return self._generate_n_random_numbers(seed,n,number_list)

	

	def generate_n_random_numbers_padron(self,n):
		padrones=int(96604+79478+84906 /3)
		number_list=[]
		return self._generate_n_random_numbers(padrones,n,number_list)
	
	def _generate_n_uniform_random_numbers(self,seed,n,number_list):
		for x in range(0,n):
			new_number= self.generate_random(seed)
			number_list.append(new_number/self.module)
			seed=new_number
		return number_list

	def generate_n_uniform_random_numbers(self,seed,n):
		number_list=[]
		return self._generate_n_uniform_random_numbers(seed,n,number_list)

	

	def generate_n_uniform_random_numbers_padron(self,n):
		padrones=int(96604+79478+84906 /3)
		number_list=[]
		return self._generate_n_uniform_random_numbers(padrones,n,number_list)