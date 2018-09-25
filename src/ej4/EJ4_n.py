import random
import math
import matplotlib.pyplot as plt
import statistics as stats

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
        u2 = random.random()
        u3 = random.random()
       
        y = l*math.log(1-u1)           
        
        if(u2 <= math.exp(-(y-1) ** 2 / 2)):
            if(u3 > 1/2):
                yaux = y * media + varianza
            else:
                yaux = -(y * media + varianza)
        lista.insert(i,yaux)
        i = i+1
 #------------------------------------------------------------
    #histograma    
    plt.hist(lista,20)
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
    moda = stats.mode(lista)
    print("MODA",moda)
 #------------------------------------------------------------   
EJ4()    
    
    
    
    
    
