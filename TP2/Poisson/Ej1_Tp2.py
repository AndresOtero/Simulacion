import numpy as np

#Opcion uno con las sos bases de datos
def OpcionUno():
  solicitudes = 100000
  tiempo_llamada_atencion = 0
  tiempo = 0
  llamada = list()
  atencion = list()

  for i in range(solicitudes):
    expllamada =  np.random.exponential(0.25)
    
    base = np.random.rand()
    
    if (base <= 0.6):
        expbase = np.random.exponential(10/7)         
    else:
        expbase = np.random.exponential(1)
        
        
    tiempo = tiempo_llamada_atencion  -  expllamada
    
    if(tiempo > 0):
        llamada.append(tiempo)
        atencion.append(tiempo + expbase)
    else:
        atencion.append(expbase)
        llamada.append(0)
    
    tiempo_llamada_atencion = expllamada + expbase
      

  return { "tiempollamada": llamada, "tiempoatencion": atencion }

#Opcion dos con la base de datos central
def OpcionDos():
  solicitudes = 100000
  tiempo_llamada_atencion = 0
  tiempo = 0
  llamada = list()
  atencion = list()
  
  for i in range(solicitudes):
      expllamada =  np.random.exponential(0.25)
      expservicio = np.random.exponential(10/8)
      
      tiempo = tiempo_llamada_atencion  -  expllamada
      
      if(tiempo > 0):
          llamada.append(tiempo)
          atencion.append(tiempo + expservicio)
      else:
          atencion.append(expservicio)
          llamada.append(0)
          
      tiempo_llamada_atencion = expllamada + expservicio     
    

  return { "tiempollamada": llamada, "tiempoatencion": atencion }
      

def CalculoAux(tiempo):
  Solicitudes_procesadas_s = tiempo.count(0) / len(tiempo)
 
  return Solicitudes_procesadas_s

def SolucionRec(tiempoOp1,tiempoOp2):
    to1 = np.mean(tiempoOp1)
    to2 = np.mean(tiempoOp2)
  
    
    relacion = to1*100/to2
    
    if(relacion >= 50):
        Sol = 'Se recomienda la opcion uno'
    else:
        Sol = 'Se recomienda la opcion dos'
        
    return Sol
    

PrimeraOpcion = OpcionUno()
SegundaOpcion = OpcionDos()
Solicitudes_procesadas_s_espera1 = CalculoAux(PrimeraOpcion["tiempollamada"])
Solicitudes_procesadas_s_espera2 = CalculoAux(SegundaOpcion["tiempollamada"])

print('Tiempo medio de espera - Opcion Uno', np.mean(PrimeraOpcion["tiempollamada"]))
print('Tiempo medio de espera - Opcion Dos',np.mean(SegundaOpcion["tiempollamada"]))

print('Solicitudes que no esperaron a ser procesadas - Opcion Uno',Solicitudes_procesadas_s_espera1)
print('Solicitudes que no esperaron a ser procesadas - Opcion Dos',Solicitudes_procesadas_s_espera2)

print('Tiempo medio de servicio - Opcion Uno', np.mean(PrimeraOpcion["tiempoatencion"]))
print('Tiempo medio de servicio - Opcion Dos', np.mean(SegundaOpcion["tiempoatencion"]))

Resolucion = SolucionRec(PrimeraOpcion["tiempoatencion"], SegundaOpcion["tiempoatencion"])

print(Resolucion)









    
    
    
    
    