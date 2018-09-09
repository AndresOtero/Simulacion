import sys
from GLC import GeneradorCongruencialLineal
from Histogram import Histogram

glc = GeneradorCongruencialLineal()
l= glc.generate_n_random_numbers_padron(6)
print (l)
l= glc.generate_n_uniform_random_numbers_padron(10)
print (l)
l= glc.generate_n_uniform_random_numbers_padron(100000)
bins=100
x_range=[0,1]
Histogram.plot(l,100,x_range,"numero","frecuencia","100.000 numeros al azar","./ej1/ej1.png")
x_range=[0,0.001]
Histogram.plot(l,100,x_range,"numero","frecuencia","100.000 numeros al azar","./ej1/ej1Zoom.png")
x_range=[0.000512,0.000514]
Histogram.plot(l,100,x_range,"numero","frecuencia","100.000 numeros al azar","./ej1/ej1ZoomPlus.png")

