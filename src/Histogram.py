
import matplotlib.pyplot as plt
 
class Histogram(object):
	"""docstring for Histogram"""
	def __init__(self):
		return
	def plot(list_of_numbers,num_bins,x_range,x_label,y_label,title,filename):
		n, bins, patches = plt.hist(list_of_numbers,bins=num_bins, facecolor='blue',range=x_range)
		plt.xlabel(x_label)
		plt.ylabel(y_label)
		plt.title(title)
		plt.grid(True)
		plt.savefig(filename)
		plt.show()
		return n,bins,patches
	def plot_without_range(list_of_numbers,num_bins,x_label,y_label,title,filename):
		n, bins, patches = plt.hist(list_of_numbers,bins=num_bins, facecolor='blue')
		plt.xlabel(x_label)
		plt.ylabel(y_label)
		plt.title(title)
		plt.grid(True)
		plt.savefig(filename)
		plt.show()
		return n,bins,patches