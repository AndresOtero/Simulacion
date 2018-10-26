import sys
sys.path.append('../')
from GLC import GeneradorCongruencialLineal
from Histogram import Histogram



p=0.5
size=10000
glc = GeneradorCongruencialLineal()

list_exp=glc.generate_n_geometrix_random_numbers_padron(size,p)
hist_bins= [i+0.5 for i in range(0,20)]
n,bins,batches=Histogram.plot_without_range(list_exp,hist_bins,"numero","frecuencia","100.00 numeros al azar","./ej6.png")

