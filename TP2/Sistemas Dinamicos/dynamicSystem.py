
class State(object):
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"

    def __init__(self, stateTuple):
        self.x=stateTuple[0]
        self.y=stateTuple[1]
        self.z=stateTuple[2]

    def getTuple(self):
        return (self.x,self.y,self.z)


class DinamicSystem(object):
    def __init__(self,firstState):
        self.state=firstState
    
    def nextState(self,state):
            self.state=state
            nextState()

    def nextState(self):
        previuosState=self.state
        x=previuosState.x /2 +previuosState.y
        y=previuosState.y - previuosState.x / 2
        z=previuosState.z - (previuosState.x + previuosState.y)
        self.state = State((x,y,z))
        return self.state   

    def setState(self,state):
        self.state=state

    def state(self):
        return self.state

    def listNextState_N_Steps(self,n):
        stateList=[]
        stateList.append(self.state.getTuple())
        for i in range(n):
            stateList.append (self.nextState().getTuple())
        return stateList