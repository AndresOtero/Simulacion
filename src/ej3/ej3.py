import sys
sys.path.append('../')
from GLC import GeneradorCongruencialLineal
from Histogram import Histogram
from numpy import log
from StaticalHelper import StaticalHelper
import math

media=0
varianza=1
glc = GeneradorCongruencialLineal()
l_random_numbers= glc.generate_n_uniform_random_numbers_padron(100000)
l_pair_random_numbers= [ (l_random_numbers[i],l_random_numbers[i]+len(l_random_numbers)/2) for i in range(len(l_random_numbers)/2)]
l_pair_random_numbers_gauss=[ box_muller(pair) for pair in l_pair_random_numbers]
l_random_numbers_gauss=[number  for pair in l_pair_random_numbers_gauss for x in pair]
n,bins,batches=Histogram.plot_without_range(l_random_numbers_gauss,100,"numero","frecuencia","100.000 numeros al azar","./ej3.png")
staticalHelper=StaticalHelper() 
mean=staticalHelper.mean(l_random_numbers_gauss)
var= staticalHelper.variance(l_random_numbers_gauss)
mode=staticalHelper.mode(l_random_numbers_gauss)
mode_freq=staticalHelper.mode_frequency(l_random_numbers_gauss)
print ("Media de la muestra:")
print (mean)
print ("Media teorica:")
print (media)
print ("Variancia de la muestra: ")
print (var)
print ("Variancia teorica:")
print (varianza)
print ("Moda de la muestra: ")
print (mode)
print ("Moda teorica:")
print (media)


def box_muller(pair):
	z1 = math.sqrt(-2 * math.log(pair[0])) * math.cos(2 * math.pi * pair[1])
	z2 = math.sqrt(-2 * math.log(pair[0])) * math.sin(2 * math.pi * pair[1])
	return (z1,z2)       