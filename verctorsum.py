import sys
from datetime import datetime
import numpy as np
"""
	This program demonstrates vector addiction the Python way.
	Run from the command line as follows

	where n is an integer that specifies the size of the vectors.

	The first vector to be added contains the squares of 0 up to n.
	The second vector contains the cubes of 0 up to n.
	The program prints the last 2 elements of the sum and the elapsed time.
	"""
def pythonsum(n):
	a=range(n)
	b=range(n)
	c=[]
	a=[i**2 for i in a];
	b=[i**3 for i in b];
	for i in range(len(a)):
		c.append(a[i]+b[i])
	return c

def numpysum(n):
	a=np.arange(n)**2
	b=np.arange(n)**3
	c=a+b
	return c

#print(int()
#size=int(sys.argv[1])
size=10000
start=datetime.now()
c=pythonsum(size)
delta=datetime.now()-start
print("The last 2 elements of the sum",c[-2:])
print("Python sum elapsed time in microseconds",delta.microseconds)


start=datetime.now()
c=numpysum(size)
delta=datetime.now()-start
print("The last 2 elements of the sum",c[-2:])
print("NumPySum elapsed time in microseconds",delta.microseconds)