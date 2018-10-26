import random
import math
import matplotlib.pyplot as plt
import statistics as stats
from statistics import mode, StatisticsError

def EJ4():    
    l = 1
    max = 100000
    c = math.sqrt(2 * math.e / math.pi)
    i = 1
    media = 35
    varianza = 5
    lista = []
    yaux = 0
    
    while (i <= max):
        u1 = random.random()
        y = l*math.log(1-u1)
        u2 = random.random()
        
        if(u2 <= math.exp(-(y-1) ** 2 / 2)):
            u3 = random.random()
            if(u3 > 1/2):
                #yaux = y * media + varianza
                yaux = y
            else:
                yaux = -y
                #yaux = -(y * media + varianza)
        lista.insert(i,yaux)
        i = i+1
 #------------------------------------------------------------
    #histograma    
    plt.hist(lista,20)
    plt.title("Histograma")
    plt.show()       
 #------------------------------------------------------------   
    #media
    media = stats.mean(lista)
    print("MEDIA:",media)
 #------------------------------------------------------------
    #varianza
    varianza = stats.variance(lista)
    print("VARIANZA:",varianza)
 #------------------------------------------------------------   
    #moda
    try:
        moda = stats.mode(lista)
    except stats.StatisticsError:
        moda = 'Moda: 0'
    print(moda)    
   
 #------------------------------------------------------------   
EJ4()    