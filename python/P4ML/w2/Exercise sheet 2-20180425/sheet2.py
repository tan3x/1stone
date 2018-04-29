
# coding: utf-8

# ## Before submitting
# 1. Before you turn this problem in, make sure everything runs as expected. First, **restart the kernel** (in the menubar, select Kernel$\rightarrow$Restart) and then **run all cells** (in the menubar, select Cell$\rightarrow$Run All).
# 
# 2. Make sure that no assertions fail or exceptions occur, otherwise points will be subtracted.
# 
# 3. Please submit only the `*.ipynb` file.
# 
# 4. Make sure you fill in any place that says `YOUR CODE HERE` or "YOUR ANSWER HERE". Edit only between `YOUR CODE HERE` and `END YOUR CODE`.
# 
# 5. Fill your group name and collaborators below:

# In[1]:

GROUPNAME = "130"
COLLABORATORS = "Taner Metin, Juhi Mehta"


# ---

# # Exercise Sheet 2: Timing, Numpy, Plotting
# 
# The previous exercise sheet introduced several methods for classification: decision trees, nearest neighbors, and nearest means. Of those, the one that could learn from the data, and that also offered enough complexity to produce an accurate decision function was k-nearest neighbors. However, nearest neighbors can be slow when implemented in pure Python (i.e. with loops). This is especially the case when the number of data points or input dimensions is large.
# 
# In this exercise sheet, we will speed up nearest neighbors by utilizing `numpy` and `scipy` packages. Your task will be to **replace list-based operations by vector-based operations** between numpy arrays. The speed and correctness of the implementations will then be tested. In particular, performance graphs will be drawn using the library `matplotlib`.
# 
# Make sure to have installed all the required packages (e.g. sklearn, scipy). For this you can e.g. use `conda install <package>` or `pip install <package>`.

# ## Python Nearest Neighbor
# 
# The most basic element of computation of nearest neighbors is its distance function relating two arbitrary data points `x1` and `x2`. We assume that these points are iterable (i.e. we can use a loop over their dimensions). One way among others to compute the square Euclidean distance between two points is by computing the sum of the component-wise distances.

# In[2]:

def pydistance(x1, x2):
    return sum([(x1d - x2d) ** 2 for x1d, x2d in zip(x1, x2)])
a1=[1,2,2]
a2=[2,3,4]
a3=zip(a1,a2)
for a,b in a3:
    print a,b
pydistance(a1,a2)


# where we use the prefix "`py-`" of the function to indicate that the latter makes use of pure `Python` instead of `numpy`. Once the distance matrix has been implemented, the nearest neighbor for a given unlabeled point `u` that we would like to classify is obtained by iterating over all points in the training set `(X, Y)`, selecting the point with smallest distance to `u`, and returning its corresponding label. Here `X` denotes the list of inputs in the training set and `Y` denotes the list of labels.

# In[3]:

def pynearest(u, X, Y, distance=pydistance):
    xbest = None
    ybest = None
    dbest = float('inf')
    for x, y in zip(X, Y):
        d = distance(u, x)
        if d < dbest:
            ybest = y
            xbest = x
            dbest = d
            
    return ybest


# Note that this function either uses function `pydistance` (given as default if the argument distance is not specified). Or one could specify as argument a more optimized function for distance compuation, for example, one that uses `numpy`. Finally, one might not be interested in classifying a single point, but many of them. The method below receives a collection of such unlabeled test points stored in the variable `U`. The function returns a list of predictions associated to each test point.

# In[4]:

def pybatch(U, X, Y, nearest=pynearest, distance=pydistance):
    return [nearest(u, X, Y, distance=distance) for u in U]


# Again, such function uses by default the Python nearest neighbor search (with a specified distance function). However, we can also specified a more optimized nearest neighbor function, for example, based on `numpy`. Finally, one could consider an alternative function to `pybatch` that would use `numpy` from the beginning to the end. The implementation of such more optimized functions, and the testing of their correct behavior and higher performance will be the object of this exercise sheet.

# ## Testing and correctness
# 
# As a starting point, the code below tests the output of the nearest neighbor algorithm for some toy dataset with fixed parameters. In particular, the function `data.toy(M,N,d)` generates a problem with `M` unlabeled test points stored in a matrix `U` of size `(M x d)`, then `N` labeled training points stored in a matrix `X` of size `(N x d)` and the output label is stored in a vector `Y` of size `N` composed of zeros and ones encoding the two possible classes. The variable `d` denotes the number of dimensions of each point. The toy dataset is pseudo-random, that is, for fixed parameters, it produce a random-looking dataset, but every time the method is called with the same parameters, the dataset is the same. The pseudo-randomness property will be useful to verify that each nearest neighbor implementation performs the same overall computation. Please check the `data.py` file within the exercise folder for the implementation details. 

# In[5]:

import data
U, X, Y = data.toy(20, 100, 50)
print 'U:', U[:1]
print 'X:', X[:1]
print 'Y:', Y[:1]
print"pybatch:", (pybatch(U, X, Y)) 


# In particular, the output of this function will help us to verify that the more optimized `numpy`-based versions of nearest neighbor are still valid.

# ## Plotting and performance
# 
# We now describe how to build a plot that relates a certain parameter of the dataset (e.g. the number of input dimensions `d` to the time required for the computation. We first initialize the basic plotting environment.

# In[6]:

import matplotlib
from matplotlib import pyplot as plt
get_ipython().magic(u'matplotlib inline')
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf', 'png')
plt.rcParams['savefig.dpi'] = 90


# The command "`%matplotlib inline`" tells IPython notebook that the plots should be rendered inside the notebook. The following code plots the computation time of predicting `100` points from the test set using a training set of size `100`, and where we vary the number of input dimensions.

# In[7]:

import time

# Values for the number of dimensions d to test
dlist = [1, 2, 5, 10, 20, 50, 100]

# Measure the computation time for each choice of number of dimensions d
tlist = []
for d in dlist:
    U, X, Y = data.toy(100, 100, d)
    a = time.clock()
    pybatch(U, X, Y)
    b = time.clock()
    tlist += [b - a]
print tlist

# Plot the results in a graph
plt.figure(figsize=(5, 3))
plt2=plt.plot(dlist, tlist, '-o')
plt.xscale('log'); plt.yscale('log'); plt.xlabel('d'); plt.ylabel('time'); plt.grid(True)


# The time on the vertical axis is in seconds. Note that the exact computation time depends on the speed of your computer. As expected, the computation time increases with the number of input dimensions. Unfortunately, for the small dataset considered here (`100` training and test points of `100` dimensions each), the algorithm already takes more than one second to execute. Thus, it is necessary for practical applications (e.g. the digit recognition task that we will consider at the end of this exercise sheet) to accelerate this nearest neighbor algorithm.

# ## 1. Accelerating the distance computation (25 P)
# 
# In this first exercise, we would like to accelerate the function that compute pairwise distances.
# 
# **a)** Create a new function `npdistance(x1,x2)` with the same output as `pydistance(x1,x2)`, but that computes the squared Euclidean distance using `numpy` operations. Verify that in both cases (i.e. using either `npdistance` or `pydistance` in the function `pybatch`) the output for the above toy example with parameters `M=20`, `N=100`, `d=50` (i.e. `data.toy(20,100,50)`) remains the same.

# In[8]:

import numpy
def npdistance(x1,x2):
    # >>>>> YOUR CODE HERE
    return numpy.sum([(x1-x2)**2 for x1, x2 in zip(x1, x2)])
    
    # <<<<< END YOUR CODE


# In[9]:

# Verify your function
assert pybatch(U, X, Y, distance=pydistance) == pybatch(U, X, Y, distance=npdistance)


# **b)** Create a plot similar to the one above, but where the computation time required by both methods are shown in a superposed manner. Here, we fix `M=100`, `N=100`, and we let `d` vary from `1` to `1000`, taking the list of values `[1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]`.

# In[10]:

# >>>>> YOUR CODE HERE
dvalues = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
tvalues = []
for d in dvalues:
    U,X,Y= data.toy(100,100,d)
    t3 = time.clock()
    pybatch(U, X, Y)
    t4 = time.clock()
    tvalues += [t4 - t3] 
    
print 'Values from pure Python:' , tlist

print 'Values from numpy:', tvalues

plt.figure(figsize=(5,3))
plt.plot(dlist, tlist, '-o', color='blue', label='pure')
plt.plot(dvalues, tvalues, '-o',color='red', label='numpy')
plt.xscale('log'); plt.yscale('log'); plt.xlabel('d'); plt.ylabel('time'); plt.grid(True)




    
# <<<<< END YOUR CODE


# In[ ]:




# **c)** Based on your results, explain what kind of speedup `numpy` provides, and in what regime do you expect the speedup to be the most important:  With several trials, it was observed that as the number of dimensions increases, numpy provides relatively quicker solution for the dataset on given range.

# In[11]:

# >>>>> YOUR CODE HERE

tdiff = []
for x in xrange(len(tlist)):
    tdiff.append(tvalues[x]-tlist[x])
print 'Value differences:', tdiff 

# <<<<< END YOUR CODE


# ## 2. Accelerating the nearest neighbor search (25 P)
# 
# Motivated by the success of the `numpy` optimized distance computation, we would like further accelerate the code by performing nearest neighbor search directly in `numpy`.
# 
# **a)** Create a new function `npnearest(u,X,Y)` as an alternative to the function `pynearest(u,X,Y,distance=npdistance)` that we have used in the previous exercise. Again, verify your function for the same toy example as before (i.e. `data.toy(20,100,50)`).

# In[12]:

def npnearest(u, X, Y, distance=npdistance):
    
    # >>>>> YOUR CODE HERE
    xbest = None
    ybest = None
    dbest = float('inf')
    for x, y in zip(X, Y):
        d = distance(u, x)
        if d < dbest:
            ybest = y
            xbest = x
            dbest = d
            
    return ybest

U, X, Y = data.toy(20, 100, 50)



    # <<<<< END YOUR CODE


# In[13]:

# Verify your function
assert pybatch(U, X, Y, nearest=pynearest) == pybatch(U, X, Y, nearest=npnearest)


# **b)** Create a plot similar to the one above, where the new method is compared to the previous one. Here, we fix `M=100`, `d=100`, and we let `N` take different values `[1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]`.

# In[24]:

# >>>>> YOUR CODE HERE
nlist =  [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
t2values = []

for N in nlist:
    U,X,Y= data.toy(100,N,100)
    t5 = time.clock()
    pybatch(U, X, Y)
    t6 = time.clock()
    t2values += [t6 - t5] 
    
print 'Values from pure Python:' , tlist

print 'Values from numpy:', tvalues

plt.figure(figsize=(5,3))
plt.plot(dlist, tlist, '-o', color='blue', label='pynearest')
plt.plot(dvalues, t2values, '-o',color='red', label='npnearest')
plt.xscale('log'); plt.yscale('log'); plt.xlabel('d'); plt.ylabel('time'); plt.grid(True)








# <<<<< END YOUR CODE


# ## 3. Accelerating the processing of multiple test points (25 P)
# 
# Not yet fully happy with the performance of the algorithm, we would like to further optimize it by avoiding performing a loop on the test points, and instead, classify them all at once.
# 
# **a)** Create a new function `npbatch(U,X,Y)` as a replacement of the implementation `pybatch(U,X,Y,nearest=npnearest)` that we have built in the previous exercise. Inside this function, use `scipy.spatial.distance.cdist` for the actual distance computation. Again, verify your function for the same toy example as before (i.e. `data.toy(20,100,50)`).

# In[28]:

def npbatch(U, X, Y, nearest=npnearest, distance=npdistance):
    # >>>>> YOUR CODE HERE

    return [nearest(u, X, Y, distance=npdistance) for u in U]
    U, X, Y = data.toy(20, 100, 50)
    
    # <<<<< END YOUR CODE


# In[29]:

assert numpy.all(pybatch(U, X, Y) == npbatch(U, X, Y))


# **b)** Create a plot comparing the computation time of the new implementation compared to the previous one. Here, we fix `N=100`, `d=100`, and we let `M` vary from `1` to `1000` with values `[1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]`.

# In[37]:

# >>>>> YOUR CODE HERE

mlist = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
t3values = []

for M in mlist:
    U,X,Y = data.toy(M,100,100)
    t7 = time.clock()
    npbatch(U, X, Y)
    t8 = time.clock()
    t3values += [t8 - t7]

plt.figure(figsize=(5, 3))
plt.plot(dvalues, t2values, '-o',color='red', label='divergant: N')
plt.plot(dvalues, t3values, '-o',color='blue', label='divergant: M')
plt.xscale('log'); plt.yscale('log'); plt.xlabel('M'); plt.ylabel('time')
plt.grid(True)
# <<<<< END YOUR CODE


# ## 4. Application to real-world data (25 P)
# 
# Having now implemented an efficient K-nearest neighbor classifier, we can test it on real problems with many data points and dimensions. We consider a small handwritten digits recognition dataset, that can be directly obtained from the library `scikit-learn`. This dataset consists of handwritten digits of size `8 x 8` flattened into arrays of size `64`, with class between `0` and `9`. We use a function `data.digits()` to load the data and arrange data points in some predefined order.

# In[83]:

X, Y = data.digits()
print 'X:' , X
print len(X)
print 'Y:' , Y
print len(Y)



# **a)** Using the function `imshow` of `matplotlib.pyplot (plt)` to visualize the first 100 digits of the dataset.

# In[76]:

def plot_first_digits():
    # >>>>> YOUR CODE HERE
    
    x100 = X[:100]
    y100 = Y[:100]
    plt.imshow(x100, aspect='auto', interpolation='none')
    
    # <<<<< END YOUR CODE
plot_first_digits()


# In[77]:

help(plt.imshow)


# **b)**
# * Partition the data into a "training" set and "test" set. The training set contains the first 1000 digits of `X`, and the test set contains the remaining ones.
# 
# * Assume that you don't know the labels for the test data and classify the test data using your efficient nearest neighbor implementation.
# 
# * Print the predicted labels for the test set.

# In[100]:

def train_test_split(x, y):
    # x are the data, y are the labels
    # >>>>> YOUR CODE HERE
    
    x_train = X[:1000]
    x_test= X[1000:-1]
    y_train = Y[:1000]
    y_test1= Y[1000:-1]
    
    # <<<<< END YOUR CODE
    return x_train, x_test, y_train, y_test

def predict(x_train, x_test, y_train):
    # >>>>> YOUR CODE HERE
    y_test=npbatch(x_test, x_train, y_train, nearest=npnearest, distance=npdistance)
    # <<<<< END YOUR CODE
    return y_test


# In[102]:

x_train, x_test, y_train, y_test1 = train_test_split(X, Y)
print(predict(x_train, x_test, y_train))


# **c)** 
# * Finally, in order to determine the accuracy of the classifier, we would like to compare the predictions with the ground truth (i.e. the true labels from the test data).
# 
# * Compute the fraction of the time on the test set where the predictions of the nearest neighbor algorithm and labels disagree. 

# In[123]:

def evaluate(x_train, x_test, y_train, y_test):
    # >>>>> YOUR CODE HERE
    ratio_disagree = 0 
    predictions = npnearest(x_test, x_train, y_train, distance=npdistance)
    for i in xrange(len(predict(x_train, x_test, y_train))):
        if Y[1000:-1] != predict(x_train, x_test, y_train):
            ratio_disagree += ratio_disagree
    # <<<<< END YOUR CODE
    print ratio_disagree
    return ratio_disagree


# In[124]:

x_train, x_test, y_train, y_test = train_test_split(X, Y)
ratio_disagree = evaluate(x_train, x_test, y_train, y_test)
assert 0 <= ratio_disagree <= 1


# In[ ]:



