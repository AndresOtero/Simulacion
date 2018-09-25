import sys
sys.path.append('../')
from mpl_toolkits.mplot3d import Axes3D
from GLC import GeneradorCongruencialLineal
import matplotlib.pyplot as plt


glc = GeneradorCongruencialLineal()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

cantNumb = 3000
numbers = glc.generate_n_uniform_random_numbers_padron(cantNumb)
x,y,z=[],[],[]
i = 0
while i < cantNumb:
    x.append(numbers[i])
    i += 1
    y.append(numbers[i])
    i += 1
    z.append(numbers[i])
    i += 1

ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.savefig("./ej7-3d.png")
plt.show()
