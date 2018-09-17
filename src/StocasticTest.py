
import matplotlib.pyplot as plt

class StocasticTest(object):
    def plot_2d(list_of_numbers,x_label,y_label,title,filename):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        x,y=[],[]
        i = 0
        while i < len(list_of_numbers):
            x.append(list_of_numbers[i])
            i += 1
            y.append(list_of_numbers[i])
            i += 1
        ax.scatter(x, y, c='r', marker='o')
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        plt.title(title)
        plt.grid(True)
        plt.savefig(filename)
        plt.show()
        
    def plot_3d(list_of_numbers,x_label,y_label,z_label,title,filename):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x,y,z=[],[],[]
        i = 0
        while i < len(list_of_numbers):
            x.append(list_of_numbers[i])
            i += 1
            y.append(list_of_numbers[i])
            i += 1
            z.append(numbers[i])
            i += 1
        ax.scatter(x, y, z, c='r', marker='o')
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_zlabel(z_label)
        plt.title(title)
        plt.grid(True)
        plt.savefig(filename)
        plt.show()
