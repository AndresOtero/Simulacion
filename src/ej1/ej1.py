import sys
sys.path.append('../')
from GLC import GeneradorCongruencialLineal
from Histogram import Histogram


glc = GeneradorCongruencialLineal()
print("Informar los primeros 6 números al azar de la secuencia.")
l= glc.generate_n_random_numbers_padron(6)
print (l)
l= glc.generate_n_uniform_random_numbers_padron(100000)
bins=100
x_range=[0,1]
n,bins,batches=Histogram.plot(l,100,x_range,"numero","frecuencia","100.000 numeros al azar","./ej1.png")
print ("Histograma 1  ")
for x in range(len(n)):
	if(n[x]>=1):
		print ("cantidad de ocurrencias: "+str(n[x])+" rango:"+str(bins[x]))
x_range=[0,0.001]
Histogram.plot(l,100,x_range,"numero","frecuencia","100.000 numeros al azar","./ej1Zoom.png")
x_range=[0.000512,0.000514]
Histogram.plot(l,100,x_range,"numero","frecuencia","100.000 numeros al azar","./ej1ZoomPlus.png")
