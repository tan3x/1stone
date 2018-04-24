import numpy as numpy
import time 
import matplotlib
import matplotlib.pyplot as plt 

t1 = time.clock()
x = [1,2,3]
y = [3,4,5]
a = numpy.ones((5,5))
b = numpy.zeros((5,5))
print a, b
print "x+y:", x+y
print "kidz songz"
t2 = time.clock()

x = numpy.arange(0, 10.001, 0.25)
y = numpy.sin(x)
z = numpy.cos(x)
plt.plot(x, y, 'o-', color='red', label='f = sin')
plt.plot(x, z, 's-', color='blue', label='f = cos')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()






   