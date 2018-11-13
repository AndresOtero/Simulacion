import matplotlib.pyplot as plt
import random
##import numpy as np

class SimulacionMarkov(object):
    def __init__(self,p,q,cantEstados,estadoInicial):
        self.pArr = p
        self.pFin = q
        self.cantEstados = cantEstados-1
        self.iteracion = 0
        self.listaEstados = []
        self.listaEstados.append(estadoInicial)
        self.estadoActual = estadoInicial
        diag1 = q*(1-p)
        diag2 = (1-p)*(1-q) + p*q
        diag3 = p*(1-q)
        
        self.matrizBase = [[0 for x in range(cantEstados)] for y in range(cantEstados)]
        self.matrizBase[0][0] = 1-p
        self.matrizBase[0][1] = p
        self.matrizBase[29][29] = (1-q) + p*q
        self.matrizBase[29][28] = q
        for i in range(1,cantEstados - 1):
            self.matrizBase[i][i-1]  = diag1
            self.matrizBase[i][i]    = diag2
            self.matrizBase[i][i+1]  = diag3           
##        self.matrizActual = self.matrizBase

    def simular(self, cantIteraciones):
        ciclo = 0
        while self.iteracion < cantIteraciones:
            self.proximoEstado()
            ciclo = ciclo + 1
            if ciclo > 1000000:
                break

    def proximoEstado(self):
        #print("Estado ", self.iteracion, " = ", self.estadoActual)
        if self.estadoActual in range(self.cantEstados+1):
            self.iteracion = self.iteracion + 1
            self.estadoActual = self.procesarEvento(self.estadoActual,self.getRandom())
            self.listaEstados.append(self.estadoActual)
##            self.matrizActual = np.multiply(self.matrizActual,self.matrizBase)

    def procesarEvento(self,i,num):
        matriz = self.matrizBase
        if i == 0:
            if num <= matriz[i][i]:
                return i
            else:
                return i+1
        elif i in range(1,self.cantEstados):
            if num <= matriz[i][i-1]:
                return i-1
            elif num <= matriz[i][i]:
                return i
            else:
                return i+1
        elif i == self.cantEstados:
            if num <= matriz[i][i-1]:
                return i-1
            else:
                return i

    def getRandom(self):
        return random.random()

    def matrizBase(self):
        return self.matrizBase

##    def matrizActual(self):
##        return self.matrizActual

    def listaEstados(self):
        return self.listaEstados

    def iteraciones(self):
        return self.iteracion

    def printResultado(self):
        for x in range(len(self.listaEstados)): 
            print ("Estado ", x, " = ", self.listaEstados[x])

    def printMatrizBase(self):
        return print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) for row in self.matrizBase]))

    def getIdleTime(self):
        idleCount = 0
        for x in range(len(self.listaEstados)):
            if self.listaEstados[x] == 0:
                idleCount = idleCount + 1
        return idleCount/self.iteraciones()
	    
    def mostrarHistogramaEstados(self, x_label,y_label,title,filename):
            n, bins, patches = plt.hist(self.listaEstados,facecolor='blue',bins=self.cantEstados)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.title(title)
            plt.grid(True)
            plt.savefig(filename)
            #plt.show()
            return n,bins,patches

    def graficarEstados(self, x_label,y_label,title,filename):
        plt.plot(self.listaEstados)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.savefig(filename)
        #plt.show()

    
