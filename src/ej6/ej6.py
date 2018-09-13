import sys
sys.path.append('../')
from GLC import GeneradorCongruencialLineal
from Histogram import Histogram
<<<<<<< HEAD
from StaticalHelper import StaticalHelper
from scipy.stats import chisquare


p=0.5
size=10000
glc = GeneradorCongruencialLineal()

list_exp=glc.generate_n_geometrix_random_numbers_padron(size,p)
hist_bins= [i+0.5 for i in range(0,20)]
n,bins,batches=Histogram.plot_without_range(list_exp,hist_bins,"numero","frecuencia","100.00 numeros al azar","./ej6.png")
=======
from numpy import log

def TirarMoneda(number):
    if (number < 0.5):
        return "cara"
    return "seca"

glc = GeneradorCongruencialLineal()
l_random_numbers= glc.generate_n_uniform_random_numbers_padron(10000)
l_custom_distribution_numbers=[ TirarMoneda(number) for number in l_random_numbers]
n,bins,batches=Histogram.plot_without_range(l_custom_distribution_numbers,3,"resultado","frecuencia","10.000 lanzamientos al azar","./ej6.png")
>>>>>>> 0c6dfcd96cb5e69cae3144223e4a16933b56810e
