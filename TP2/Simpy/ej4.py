import random

import simpy
import matplotlib.pyplot as plt
from Histogram import Histogram


RANDOM_SEED = 42
#EXPONENTIAL_MEAN = 45 
SECONDS_PER_HOUR=3600
EXPONENTIAL_MEAN_SOURCE_TIME_TUPLE_LIST=[(240,2),(120,5),(360,9)]
class Source(object):
    def __init__(self,env, exponentialMean, atm,timeUntil):
        self.env=env
        self.exponentialMean=exponentialMean
        self.atm=atm
        self.timeUntil=timeUntil

    def startServingCustomers(self):
        while True:
            print("Source" +str(exponentialMean)+" "+str(env.now) + " "+ str(self.timeUntil))
            if(env.now>self.timeUntil):
                break
            t = random.expovariate(1.0 / self.exponentialMean)
            yield env.timeout(t)
            c = Customer(self.env,self.atm)
            env.process(c.useATM())


        return

class Customer(object):
    maxQueueLength=0
    timeMaxQueueLength=[]
    customerNumber=0.0
    maxWaitingTime=0.0
    clientTypemaxWaitingTime=0
    maxWaitingTimeQueueLen=0
    timeMaxWaitingTime=0
    servedCustomers = []
    arrivedCustomers=[]
    def __init__(self,env,atm):
        self.env=env
        self.atm=atm
        customerType,processTime =self.generateCustomerType()
        self.customerType=customerType
        self.processTime=processTime
        Customer.customerNumber+=1
        self.startWaiting=env.now

    def generateCustomerType(self):
        uVariable=random.uniform(0,1)
        if(uVariable<0.1):
            processTime= (4 +random.uniform(-3,3))*60
            return 1,processTime
        if(uVariable<0.8):
            processTime= (2 +random.uniform(-1,1))*60
            return 2,processTime
        processTime= (3 +random.uniform(-2,2))*60
        return 3,processTime



    def useATM(self):
        """Customer arrives, is served and leaves."""
        arrive = env.now
        cstNumber=Customer.customerNumber
        print('%7.4f Cliente Nro %s arrived, type: %s' % (arrive, str(cstNumber),str(self.customerType)))
        queueLength=len(self.atm.queue)
        print("Queue length %s"%str(queueLength))

        if(Customer.maxQueueLength<queueLength):
            Customer.timeMaxQueueLength.clear()
            Customer.maxQueueLength=queueLength

        if(Customer.maxQueueLength==queueLength):
            Customer.timeMaxQueueLength.append(env.now)
        Customer.arrivedCustomers.append((cstNumber,self.customerType,arrive,queueLength))
        with self.atm.request() as req:
            yield req 

            waitingTime=env.now-arrive
            yield env.timeout(self.processTime)
            print('Cliente Nro %s arrived, arrive: %s ,Process time : %s , Waiting time : %s ' % ( str(cstNumber),arrive,str(self.processTime),str(waitingTime)))
            if Customer.maxWaitingTime<waitingTime :
                Customer.maxWaitingTime=waitingTime
                Customer.clientTypemaxWaitingTime=self.customerType
                Customer.maxWaitingTimeQueueLen=queueLength
                Customer.timeMaxWaitingTime=arrive
        Customer.servedCustomers.append((cstNumber,self.customerType,arrive,queueLength,waitingTime,self.processTime))



random.seed(RANDOM_SEED)
env = simpy.Environment()

# Start processes and run
atm = simpy.Resource(env, capacity=1)
for exponentialMean,sourceTime in EXPONENTIAL_MEAN_SOURCE_TIME_TUPLE_LIST:
    print ("Proceso inicia",exponentialMean,sourceTime,sourceTime*SECONDS_PER_HOUR)
    source=Source(env, exponentialMean, atm,sourceTime*SECONDS_PER_HOUR)
    env.process(source.startServingCustomers())
    env.run(until=sourceTime*SECONDS_PER_HOUR)
env.run()
print("Max queue length: %s , times it happend: %s"%(Customer.maxQueueLength,str(Customer.timeMaxQueueLength)))
print("Max waiting time: %s , type of customer: %s ,time it happend: %s , queue len: %s "%(Customer.maxWaitingTime,Customer.clientTypemaxWaitingTime,str(Customer.timeMaxWaitingTime),str(Customer.maxWaitingTimeQueueLen)))
arrive=[10 + x[2]/3600 for x in Customer.servedCustomers]
waitingTime=[x[4] for x in Customer.servedCustomers]
queueLen=[x[3] for x in Customer.servedCustomers]
cstNumber=[x[0] for x in Customer.arrivedCustomers]
cstType=[x[1] for x in Customer.arrivedCustomers]
processTime=[x[5] for x in Customer.servedCustomers]

f, axarr = plt.subplots(3, sharex=True)
axarr[0].plot(arrive, waitingTime)
axarr[0].set_xlabel("tiempo")
axarr[0].set_ylabel("Tiempo de espera")
axarr[1].plot(arrive, queueLen)
axarr[1].set_xlabel("tiempo")
axarr[1].set_ylabel("Fila")
axarr[2].scatter(arrive, cstType)
axarr[2].set_xlabel("tiempo")
axarr[2].set_ylabel("Tipo de cliente")
plt.show()
