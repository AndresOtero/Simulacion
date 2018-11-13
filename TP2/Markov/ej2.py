import SimulacionMarkov as Simulador

p = 1/30
q = 1/40

simulador = Simulador.SimulacionMarkov(p,q,30,0)
simulador.simular(100000)
print("Porcentae de tiempo sin procesar solicitudes: ", simulador.getIdleTime())
simulador.mostrarHistogramaEstados("Estado","Cantidad","Histograma de Estados","./ej2-hist.png")
simulador.graficarEstados("Iteracion","Estado","Evolución de Estados","./ej2-grafico.png")


