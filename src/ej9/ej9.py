import sys
sys.path.append('../')
from GLC import GeneradorCongruencialLineal

def count_gap(glc,a,b,size):
    cont = 0
    if a >= 0 and b <= 1 and a < b and size > 0:
        numbers = glc.generate_n_uniform_random_numbers_padron(size)
        for i in range(1,size):
            if numbers[i] >= a and numbers[i] <= b:
                cont += 1
    return cont

def test_gap(glc,a,b,size):
    if a >= 0 and b <= 1 and a < b and size > 0:
        valores_dentro_gap = count_gap(glc,a,b,size)
        print ("Test Gap entre ", a, " y ", b)
        print ("Valores totales: ", size)
        esperados = (b - a) * size
        print ("Valores esperados dentro del gap: ", esperados)
        print ("Valores obtenidos dentro del gap: ", valores_dentro_gap)
        porcentaje = "{:.1%}".format(1-(esperados/valores_dentro_gap))
        print ("Porcentaje de significación: ", porcentaje)
    else:
        print ("Parámetros inválidos")

glc = GeneradorCongruencialLineal()
test_gap(glc,0.5,1,2000)

test_gap(glc,0.2,0.6,2000)
