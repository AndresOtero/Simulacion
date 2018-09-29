import sys
sys.path.append('../')
import random
import math
import matplotlib.pyplot as plt
import statistics as stats
import scipy.stats as ss
from scipy import stats
from Histogram import Histogram
from matplotlib import pyplot

def EJ10():
    l = 1
    max = 10000
    c = math.sqrt(2 * math.e / math.pi)
    i = 1
    media = 35
    varianza = 5
    lista = []
    yaux = 0
    alfa = 0.01
    
    while (i <= max):
        u1 = random.random()
        y = l*math.log(1-u1)
        u2 = random.random()
        
        if(u2 <= math.exp(-(y-1) ** 2 / 2)):
            u3 = random.random()
            if(u3 > 1/2):
                yaux = y * media + varianza
                #yaux = y
            else:
                #yaux = -y
                yaux = -(y * media + varianza)
        lista.insert(i,yaux)
        i = i+1
#-----------------------------------------------------------------------------    
    media, desviacion = ss.norm.fit(lista)
    d, pvalor = stats.kstest(lista,"norm",args=(media,desviacion))
    print(pvalor)
    if pvalor < alfa:
        print("Se acepta la H0 , la distribucion sigue una normal")
    else:
        print("No se acepta H0, la distribucion no sigue una normal")
        
    hist_bins= [i+0.5 for i in range(0,30)]
    n,bins,batches=Histogram.plot_without_range(lista,hist_bins,"numero","frecuencia","100.00 numeros al azar","./ej10.png")
    
    
EJ10()