import matplotlib.pyplot as plt
from dynamicSystem import State
from dynamicSystem import DinamicSystem
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

listNumbers=[1,0,-1]
possibleStates= [ (x,y,z) for x in listNumbers for y in listNumbers for z in listNumbers]
arrayTrajectories={}
for possState in possibleStates:
	state=State(possState)
	dinamicSystem=DinamicSystem(state)
	arrayTrajectories[possState]=dinamicSystem.listNextState_N_Steps(100)

fig = plt.figure()
ax = fig.gca(projection='3d')
for possState in arrayTrajectories: 
	ax.scatter3D(possState[0],possState[1],possState[2])
	x= [ x[0] for x in arrayTrajectories[possState]]
	y= [ x[1] for x in arrayTrajectories[possState]]
	z= [ x[2] for x in arrayTrajectories[possState]]
	ax.plot(x, y, z, label=str(possState))

x= [ 0 for x in range(100)]
y= [ 0 for x in range(100)]
z= [ x/5.0 for x in range(-50,50)]
ax.plot(x, y, z, label="eje z")
ax.legend()
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.grid(True)		
plt.savefig(str("todo")+".png")
plt.show()
