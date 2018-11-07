import random

import simpy


RANDOM_SEED = 42
#EXPONENTIAL_MEAN = 45 
SECONDS_PER_HOUR=3600
EXPONENTIAL_MEAN_SOURCE_TIME_TUPLE_LIST=[(240,2),(120,5),(360,9)]
class Source(object):
    maxQueueLength=0
    timeMaxQueueLength=[]
    def __init__(self,env, exponentialMean, atm):
        self.env=env
        self.exponentialMean=exponentialMean
        self.atm=atm

    def startServingCustomers(self):
        while True:
            c = Customer(self.env,self.atm)
            env.process(c.useATM())
            t = random.expovariate(1.0 / self.exponentialMean)

            yield env.timeout(t)

class Customer(object):
    maxQueueLength=0
    timeMaxQueueLength=[]
    customerNumber=0.0
    maxWaitingTime=0.0
    clientTypemaxWaitingTime=0
    timeMaxWaitingTime=0
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
        print("Queue length %s"%queueLength)

        if(Customer.maxQueueLength<queueLength):
            Customer.timeMaxQueueLength.clear()
            Customer.maxQueueLength=queueLength

        if(Customer.maxQueueLength==queueLength):
            Customer.timeMaxQueueLength.append(env.now)

        with self.atm.request() as req:
            yield req 

            waitingTime=env.now-arrive
            yield env.timeout(self.processTime)
            print('Cliente Nro %s arrived, Process time : %s' % ( str(cstNumber),str(env.now-arrive)))
            print('Cliente Nro %s arrived, Waiting time : %s' % ( str(cstNumber),str(waitingTime)))
            if Customer.maxWaitingTime<waitingTime :
                Customer.maxWaitingTime=waitingTime
                Customer.clientTypemaxWaitingTime=self.customerType
                Customer.timeMaxWaitingTime=arrive



# Setup and start the simulation
random.seed(RANDOM_SEED)
env = simpy.Environment()

# Start processes and run
atm = simpy.Resource(env, capacity=1)
for exponentialMean,sourceTime in EXPONENTIAL_MEAN_SOURCE_TIME_TUPLE_LIST:
    print (exponentialMean,sourceTime)
    source=Source(env, exponentialMean, atm)
    env.process(source.startServingCustomers())
    env.run(until=sourceTime*SECONDS_PER_HOUR)
    print("Termino Proceso")
print("Max queue length: %s , times it happend: %s"%(Customer.maxQueueLength,str(Customer.timeMaxQueueLength)))
print("Max waiting time: %s , type of customer: %s ,time it happend: %s"%(Customer.maxWaitingTime,Customer.clientTypemaxWaitingTime,str(Customer.timeMaxWaitingTime)))