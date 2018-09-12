import sys
sys.path.append('../')
from GLC import GeneradorCongruencialLineal
from Histogram import Histogram
from numpy import log
from StaticalHelper import StaticalHelper
import math
def getValueBack(number):
	if(number<0.5):
		return 1
	if (number<0.7):
		return 2
	if (number<0.8):
		return 3
	return 4

glc = GeneradorCongruencialLineal()
l_random_numbers= glc.generate_n_uniform_random_numbers_padron(100000)
l_custom_distribution_numbers=[ getValueBack(number) for number in l_random_numbers]
n,bins,batches=Histogram.plot_without_range(l_custom_distribution_numbers,8,"numero","frecuencia","100.000 numeros al azar","./ej5.png")
