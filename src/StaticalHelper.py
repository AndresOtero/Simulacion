from numpy import mean
from numpy import var
from scipy import stats
 
class  StaticalHelper(object) :
	
	def __init__ (self):
		return

	def mean(self, list_of_numbers):
		return mean(list_of_numbers)

	def variance(self,list_of_numbers):
		return var(list_of_numbers)

	def mode(self,list_of_numbers):
		return stats.mode(list_of_numbers)[0][0]

	def mode_frequency(self,list_of_numbers):
		return stats.mode(list_of_numbers)[1][0]