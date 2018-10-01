import sys
sys.path.append('../')
import matplotlib.pyplot as plt
import numpy as np
from GLC import GeneradorCongruencialLineal
from scipy import interpolate
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import interp1d
import statistics as stats
import statistics
from statistics import mode, StatisticsError

def EJ3():
    glc = GeneradorCongruencialLineal()
   
    numbers = glc.generate_n_uniform_random_numbers_padron(100000)
    listax = []
    listay = []
    modas = [] 
    
    listax = [0, 0.00003, 0.00135, 0.00621, 0.02275, 0.06681, 0.11507, 0.15866,
              0.21186, 0.27425, 0.34458, 0.42074, 0.5, 0.57926, 0.65542, 0.72575,
              0.78814, 0.84134,0.88493,0.93319, 0.97725, 0.99379, 0.99865, 0.99997, 1]
    
    listay = [-5, -4, -3, -2.5, -2, -1.5, 1.2, -1, -0.8, -0.6, -0.4,
              -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.5, 2, 2.5, 3, 4, 5]
    
    listainterp = np.interp(numbers, listax,listay)
    plt.hist(listainterp,20)
    plt.title("Histograma")
    plt.show()
    
#------------------------------------------------------------------------------------------
    #Calculo la media
    media = stats.mean(listainterp)
    print("MEDIA:",media)
#-------------------------------------------------------------------------------------------
    #Calculo la varianza
    varianza = stats.variance(listainterp)
    print("VARIANZA:",varianza)
#------------------------------------------------------------------------------------------
    try:
        print("MODA" + stats.mode(listainterp))
  
    except StatisticsError:
        print("MODA:" + "0")
#--------------------------------------------------------------------------------------------
    #Comparacion distribucion normal brindada por python VS. distribucion obtenida   
    y1 = np.random.normal(-2,2,100000)
    
    colors = ['b','g']
    fig, ax1 = plt.subplots()
    ax1.hist([y1,listainterp],color=colors)
    ax1.set_xlim(-10,10)
    plt.tight_layout()
    plt.title("Histograma")
    plt.show()
       
EJ3()