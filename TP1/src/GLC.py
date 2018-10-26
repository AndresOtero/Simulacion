from numpy import log


class  GeneradorCongruencialLineal(object) :
	

	def __init__(self, multiplier, increment, module):
		self.multiplier = multiplier
		self.increment = increment
		self.module = module
		self.seed =None

	def __init__ (self):
		self.multiplier = 1013904223
		self.increment = 1664525
		self.module = 2**32
		self.seed=None

	def set_seed(self,seed):
		self.seed=seed

	def set_seed_padron(self):
		self.seed=int(96604+79478+84906 /3)

	def has_seed(self):
		return (self.seed!=None)

	def generate_random(self):
		if(not self.has_seed()):
			raise Exception('Must set seed')
		new_number=(self.multiplier*self.seed+self.increment)%self.module
		self.seed=new_number #guarda la semilla
		return new_number

	def generate_random_padron(self):
		self.set_seed_padron()
		return self.generate_random()

	def generate_random_uniform(self):
		new_number=self.generate_random()
		return (new_number)/self.module


	def generate_random_bernoulli(self,p):
		new_number=self.generate_random_uniform()
		if(new_number<p):
			return 0
		else:
			return 1

	def generate_random_geometric(self,p):
		new_number=self.generate_random_bernoulli(p)
		k=1
		while (new_number!=0):
			new_number=self.generate_random_bernoulli(p)
			k+=1
		return k

	

	def _generate_n_random_numbers(self,seed,n,number_list):
		self.set_seed(seed)
		print (self.seed)
		for x in range(0,n):
			new_number= self.generate_random()
			number_list.append(new_number)
		return number_list

	def generate_n_random_numbers(self,seed,n):
		number_list=[]
		return self._generate_n_random_numbers(seed,n,number_list)

	

	def generate_n_random_numbers_padron(self,n):
		padrones=int(96604+79478+84906 /3)
		number_list=[]
		return self._generate_n_random_numbers(padrones,n,number_list)
	
	def _generate_n_uniform_random_numbers(self,seed,n,number_list):
		self.set_seed(seed)
		for x in range(0,n):
			number_list.append( self.generate_random_uniform())
		return number_list

	def generate_n_uniform_random_numbers(self,seed,n):
		number_list=[]
		return self._generate_n_uniform_random_numbers(seed,n,number_list)

	def generate_n_uniform_random_numbers_padron(self,n):
		padrones=int(96604+79478+84906 /3)
		number_list=[]
		return self._generate_n_uniform_random_numbers(padrones,n,number_list)
	
	def generate_n_exp_random_numbers(self,seed,n,media):
		l_random_numbers= self.generate_n_uniform_random_numbers(seed,n)
		list_exp=[ log(1-x)/(-1/media) for x in l_random_numbers]
		return list_exp

	def generate_n_exp_random_numbers_padron(self,n,media):
		l_random_numbers= self.generate_n_uniform_random_numbers_padron(n)
		list_exp=[ log(1-x)/(-1/media) for x in l_random_numbers]
		return list_exp


	def generate_n_geometic_random_numbers(self,seed,n,p):
		self.set_seed(seed)
		list_geo=[ self.generate_random_geometric(p) for x in range(n)]
		return list_geo

	def generate_n_geometrix_random_numbers_padron(self,n,p):
		self.set_seed_padron()
		list_geo=[ self.generate_random_geometric(p) for x in range(n)]
		return list_geo

