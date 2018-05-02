
# coding: utf-8

# In[1]:

import numpy 


# In[2]:

x = numpy.array([1,2,2,3,4])


# In[3]:

y = numpy.array([3,5,6,7,8])


# In[10]:

x * y #element-wise multiplication


# In[11]:

x.T


# In[13]:

x[2:]


# In[52]:

numpy.dot(x,y) #dot product, matrix multiplication


# In[53]:

numpy.dot(x,x.T)


# In[22]:

x_list=[1,2,2,3,4]


# In[23]:

y_list=[3,5,6,7,8]


# In[25]:

x_list + y_list #extending addition


# In[28]:

x_list * y_list #raises exception, since list is not a real array


# In[41]:

zip(x_list,y_list) #pair presentation of list


# In[45]:

s = [a+b for a,b in zip(x_list,y_list)] #element-wise addition of list


# In[47]:

print sum(s)


# In[49]:

type(s)


# In[58]:

A = numpy.array(
        [
        [1,2,3],
        [4,5,6]
        ]
)


# In[63]:

print A
print (10 * "ß")
print A.shape


# In[65]:

A * A # element-wise


# In[68]:

numpy.dot(A,A.T) #matrix-multiplication


# In[69]:

import time


# In[71]:

time.clock()


# In[81]:

def benchmark_python(n):
    #initials
    x1 = numpy.ones((n,n))
    x2 = numpy.ones((n,n))
    x3 = numpy.zeros((n,n))
    
    #actual multiplication
    start = time.clock()
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                x3[i,j] = x1[i,k] * x2[k,j]
    end  = time.clock()
    return end-start



# In[127]:

def benchmark_numpy(n):
    x1 = numpy.ones((n,n))
    x2 = numpy.ones((n,n))
    x3 = numpy.zeros((n,n))
    
    start = time.clock()
    
    z = numpy.dot(x1,x2)
    
    end = time.clock()
    
    return end-start
        


# In[128]:

size=100
benchmark_python(size), benchmark_numpy(size)


# In[129]:

import matplotlib
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[ ]:




# In[130]:

xA = numpy.arange(0,10.01, 0.25)
xSin = numpy.sin(xA)
xCos = numpy.cos(xA)


# In[131]:

print x4


# In[132]:

plt.plot(xA, xSin, 'o-', color='red', label='f = sin(x)')
plt.plot(xA, xCos, 'o-', color='blue', label='f = cos(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)


# In[133]:

N = [1, 2, 4, 8, 16, 32, 64, 128, 256]


# In[136]:

py_t = [benchmark_python(n) for n in N]
np_t = [benchmark_numpy(n) for n in N]


# In[137]:

plt.plot(N, py_t, 'o-', label='Python')
plt.plot(N, np_t, 's-', label='Numpy')
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('array size n')
plt.ylabel('time [s]')
plt.legend(loc='lower right')


# In[152]:

A = numpy.zeros((3, 3)) # array of size 2x2 filled with zeros
A3 = numpy.zeros((3, 3, 3)) # array of size 2x2 filled with zeros
B = numpy.ones((3, 3)) # same, but filled with ones
C = numpy.diag((1.0, 2.0, 3.0)) # diagonal matrix
D = numpy.eye(3) # identity matrix
E = numpy.random.rand(3, 3) # random numbers
F = numpy.triu(B) # upper triagonal matrix


# In[153]:

print C


# In[156]:

A3.shape


# In[157]:

from sklearn.datasets import load_boston


# In[158]:

boston = load_boston()


# In[162]:

print boston.keys()


# In[208]:

D = boston['data']
F = boston['feature_names']


# In[209]:

print D
print F


# In[210]:

print(D[:,0].mean())
print(D[:,0])


# In[211]:

(zip(F, D.mean(axis=0), D.std(axis=0))) #creating list


# In[212]:

D = D[:, [5, 12]]
plt.figure(figsize=(6,6))
plt.plot(D[:, 0], D[:, 1], 'o', color='black', ms=3)
plt.plot(D[:, 0].mean(), D[:, 1].mean(), 'o', color='red', ms=10)


# In[202]:

D_norm = D - D.mean(axis=0) # center around origin
D_norm /= D.std(axis=0) # rescale features


# In[213]:

import scipy
import scipy.spatial


# In[214]:

S = scipy.spatial.distance.cdist(D_norm, D_norm)


# In[215]:

print S


# In[218]:

plt.figure(figsize=(6, 6))
ind = numpy.where(S < 0.2)


# In[220]:

plt.plot(D_norm[:, 0], D_norm[:, 1], 'o', color='black', ms=3)


# In[233]:

for i1,i2 in zip(*ind):
    plt.plot([D_norm[i1, 0], D_norm[i2, 0]], [D_norm[i1, 1], D_norm[i2, 1]], color='red')


# In[231]:

help(numpy.where)


# In[ ]:



