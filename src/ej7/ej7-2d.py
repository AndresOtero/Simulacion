from mpl_toolkits.mplot3d import Axes3D
from GLC import GeneradorCongruencialLineal
import matplotlib.pyplot as plt


glc = GeneradorCongruencialLineal()
fig = plt.figure()
ax = fig.add_subplot(111)

cantNumb = 2000
numbers = glc.generate_n_uniform_random_numbers_padron(cantNumb)
x,y=[],[]
i = 0
while i < cantNumb:
    x.append(numbers[i])
    i += 1
    y.append(numbers[i])
    i += 1

ax.scatter(x, y, c='r', marker='o')

ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.savefig("./ej7-2d.png")
plt.show()
