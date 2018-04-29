
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

num_dimensions=100
benchmark_python(num_dimensions), benchmark_numpy(num_dimensions)


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


# In[ ]:




# In[ ]:



