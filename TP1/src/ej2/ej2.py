import sys
sys.path.append('../')
from GLC import GeneradorCongruencialLineal
from Histogram import Histogram
from StaticalHelper import StaticalHelper



media=15
n=100000
glc = GeneradorCongruencialLineal()

list_exp=glc.generate_n_exp_random_numbers_padron(n,media)
n,bins,batches=Histogram.plot_without_range(list_exp,100,"numero","frecuencia","100.000 numeros al azar","./ej2.png")
# print ("Histograma 1  ")
# for x in range(len(n)):
# 	if(n[x]>=1):
# 		print ("cantidad de ocurrencias: "+str(n[x])+" rango:"+str(bins[x]))
staticalHelper=StaticalHelper() 
mean=staticalHelper.mean(list_exp)
var= staticalHelper.variance(list_exp)
mode=staticalHelper.mode(list_exp)
mode_freq=staticalHelper.mode_frequency(list_exp)
print ("Media de la muestra:")
print (mean)
print ("Media teorica:")
print (media)
print ("Variancia de la muestra: ")
print (var)
print ("Variancia teorica:")
print (media**2)
print ("Moda de la muestra: ")
print (mode)
print ("Moda teorica:")
print (0)


