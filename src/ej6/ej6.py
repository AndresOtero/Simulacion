import sys
sys.path.append('../')
from GLC import GeneradorCongruencialLineal
from Histogram import Histogram
from numpy import log

def TirarMoneda(number):
    if (number < 0.5):
        return "cara"
    return "seca"

glc = GeneradorCongruencialLineal()
l_random_numbers= glc.generate_n_uniform_random_numbers_padron(10000)
l_custom_distribution_numbers=[ TirarMoneda(number) for number in l_random_numbers]
n,bins,batches=Histogram.plot_without_range(l_custom_distribution_numbers,3,"resultado","frecuencia","10.000 lanzamientos al azar","./ej6.png")
