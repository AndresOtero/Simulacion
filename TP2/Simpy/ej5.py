import random

import sys

import simpy

import itertools

EXPONENTIAL_MEAN=45
NUMBER_OF_SERVERS=5
NUMBER_OF_REQUESTS=1000


class Sender(object):
    maxQueueLength=0
    timeMaxQueueLength=[]
    def __init__(self,env, exponentialMean, loadBalancer,numberOfRequests):
        self.env=env
        self.exponentialMean=exponentialMean
        self.loadBalancer=loadBalancer
        self.numberOfRequests=numberOfRequests

    def startSendingRequests(self):
        for x in range(self.numberOfRequests):
        	t = random.expovariate(1.0 / self.exponentialMean)
        	yield env.timeout(t)
        	req = Request(self.env)
        	server = self.loadBalancer.get()
        	self.env.process(server.sendRequest(req))

class Server(object):
	serverNumber=0
	def __init__(self,env):
		self.env=env
		self.srvNr =Server.serverNumber
		Server.serverNumber+=1
		self.server= simpy.Resource(env, capacity=1)
		self.requestsServed=[]
        #self.startWaiting=env.no
	def sendRequest(self,request):
		arrive = self.env.now
		#print('Server Nro %s ,Request Nro %s arrived at time : %s' % (str(self.srvNr), str(request.custNr),str(env.now)))
		with self.server.request() as req:
			yield req
			serverReceived=self.env.now
			yield env.timeout(request.processTime)
			print('Server Nro %s ,Request Nro %s , type %s ,arrived at %s ,left at %s, Process time : %s  ,Waiting time : %s , queue len: %s' % (str(self.srvNr), str(request.custNr),str(request.customerType),str(arrive),str(env.now),str(self.env.now-serverReceived),str(serverReceived-arrive),str(self.getQueueLen())))
			#print('Server Nro %s, Queue Length: %s' % (str(self.srvNr), len(self.server.queue)))
			self.requestsServed.append((str(self.srvNr), str(request.custNr),str(request.customerType),str(arrive),str(env.now),str(self.env.now-serverReceived),str(serverReceived-arrive),str(self.getQueueLen())))

	def getQueueLen(self):
		return len(self.server.queue)

class Request(object):
    
    requestNumber=0
    maxWaitingTime=0.0
    clientTypemaxWaitingTime=0
    timeMaxWaitingTime=0
    def __init__(self,env):
        self.env=env
        customerType,processTime =self.generateCustomerType()
        self.customerType=customerType
        self.processTime=processTime
        self.custNr =Request.requestNumber
        Request.requestNumber+=1
        #print('Request Nro %s, type %s ' % (str(self.custNr),str(self.customerType)))
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

class  LoadBalancer(object):
	"""docstring for  loadBalancer"""
	def __init__(self, numberOfServers,loadBalancerType):
		self.store= simpy.FilterStore(env, capacity=numberOfServers)
		self.servers=[]
		self.loadBalancerType=loadBalancerType
		self.cycleIter=itertools.cycle(self.servers)

	def put(self,server):
		self.servers.append(server)
		self.cycleIter=itertools.cycle(self.servers)

	def get(self):
		if(self.loadBalancerType=="0"):
			#self.servers.sort(key=lambda server: server.srvNr)
			self.servers.sort(key=lambda server: server.getQueueLen())
			#print([("Server "+str(server.srvNr),server.getQueueLen()) for server in self.servers])
			#print ("Elijo "+ str( self.servers[0].srvNr))
			choosenServer= self.servers[0]
			#print ("El load balancer tipo 0 eligio el servidor "+str(choosenServer.srvNr)+ " con carga "+str(choosenServer.getQueueLen()))
			return choosenServer
		else:
			choosenServer= next(self.cycleIter)
			#print ("El load balancer tipo 1 eligio el servidor "+str(choosenServer.srvNr)+ " con carga "+str(choosenServer.getQueueLen()))
			return choosenServer


random.seed(42)
env = simpy.Environment()
loadBalancerType=sys.argv[1]
numberOfRequests	=  int(sys.argv[2]) if (len(sys.argv)>2)  else NUMBER_OF_REQUESTS
loadBalancer = LoadBalancer(NUMBER_OF_SERVERS,loadBalancerType)
for i in range(NUMBER_OF_SERVERS):
	server=Server(env)
	loadBalancer.put(server)



sender=Sender(env,EXPONENTIAL_MEAN,loadBalancer,numberOfRequests)
env.process(sender.startSendingRequests())
env.run()
print("Finalizo:"+str(env.now))
for server in loadBalancer.servers:
	print("El server %s contesto %s requests" % ((server.srvNr,str(len(server.requestsServed)))))
