import sys
sys.path.append('../')
from GLC import GeneradorCongruencialLineal
from Histogram import Histogram
from StaticalHelper import StaticalHelper
from scipy.stats import chisquare


p=0.5
size=10000
glc = GeneradorCongruencialLineal()

list_exp=glc.generate_n_geometrix_random_numbers_padron(size,p)
hist_bins= [i+0.5 for i in range(0,30)]
n,bins,batches=Histogram.plot_without_range(list_exp,hist_bins,"numero","frecuencia","100.00 numeros al azar","./ej6.png")
print ("observed values",n)
expected_value=[ ((1-p)**(i-1))*p*size for i in range(1,30)]
print ("expected values",expected_value)
print(chisquare(n,f_exp=expected_value))