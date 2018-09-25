import math
import matplotlib.pyplot as plt
import statistics as stats

def EJ3():
    a = 1013904223
    c = 1664525
    x = 86996
    m = 2**32
    
    lista = []
    
    for i in range(100000):
         x = (a*x + c) % m
         u =  x/m
        
         z = math.sqrt(2) * math.erf(-1) * (2*u - 1)
         lista.insert(i,z)
#-------------------------------------------------------
    #histograma     
    plt.hist(lista,20)
    plt.title('HISTOGRAMA')
    plt.show()      
#-------------------------------------------------------
    #------------------------------------------------------------   
    #media
    media = stats.mean(lista)
    print("MEDIA:",media)
 #------------------------------------------------------------
    #varianza
    varianza = stats.variance(lista)
    print("VARIANZA:",varianza)
 #------------------------------------------------------------   
    moda
    moda = stats.mode(lista)
    print("MODA",moda)
 #------------------------------------------------------------   
    
    
EJ3()    