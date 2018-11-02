import random

import simpy

EXPONENTIAL_MEAN=45

class Sender(object):
    maxQueueLength=0
    timeMaxQueueLength=[]
    def __init__(self,env, exponentialMean, loadBalancer,numberOfRequests):
        self.env=env
        self.exponentialMean=exponentialMean
        self.loadBalancer=loadBalancer
        self.numberOfRequests=numberOfRequests

    def startSendingRequests(self):
        for x in range(numberOfRequests):
            req = Request(self.env,self.atm)
            env.process(c.useATM())
            t = random.expovariate(1.0 / self.exponentialMean)
            queueLength=len(self.atm.queue)
            print("Queue length %s"%queueLength)

            if(Source.maxQueueLength<queueLength):
                Source.timeMaxQueueLength.clear()
                Source.maxQueueLength=queueLength

            if(Source.maxQueueLength==queueLength):
                Source.timeMaxQueueLength.append(env.now)

            yield env.timeout(t)


class Request(object):
    
    requestNumber=0.0
    maxWaitingTime=0.0
    clientTypemaxWaitingTime=0
    timeMaxWaitingTime=0
    def __init__(self,env):
        self.env=env
        customerType,processTime =self.generateCustomerType()
        self.customerType=customerType
        self.processTime=processTime
        Customer.customerNumber+=1
        self.custNr =Customer.customerNumber
        #self.startWaiting=env.now

    def generateCustomerType(self):
        uVariable=random.uniform(0,1)
        if(uVariable<0.7):
            processTime= (120 +random.uniform(-60,60))
            return "A",processTime
        if(uVariable<0.9):
            processTime= (240 +random.uniform(-120,120))
            return "B",processTime
        processTime= (500 +random.uniform(-300,300))
        return "C",processTime

	def sendRequest(self,server):
		with self.atm.request() as req:
            yield req 
            yield env.timeout(self.processTime)
            
		