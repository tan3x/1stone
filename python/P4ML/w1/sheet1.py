
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

GROUPNAME = ""
COLLABORATORS = "Taner Metin"


# ---

# # Exercise Sheet 1: Python Basics
# 
# This first  exercise sheet tests the basic functionalities of the Python programming language in the context of a simple prediction task. We consider the problem of predicting health risk of subjects from personal data and habits. We first use for this task a decision tree
# 
# ![](tree.png)
# 
# adapted from the webpage http://www.refactorthis.net/post/2013/04/10/Machine-Learning-tutorial-How-to-create-a-decision-tree-in-RapidMiner-using-the-Titanic-passenger-data-set.aspx. For this exercise sheet, you are required to use only pure Python, and to not import any module, including numpy. In exercise sheet 2, the nearest neighbor part of this exercise sheet will be revisited with numpy.

# ## Classifying a single instance (15 P)
# 
# * Create a function that takes as input a tuple containing values for attributes (smoker,age,diet), and computes the output of the decision tree. Should return `"less"` or `"more"`.
# * Test your function on the tuple `('yes', 31, 'good')`,

# In[47]:

def decision(x):
    # >>>>> YOUR CODE HERE
    #N= tuple(raw_input().split(','))
    
    
    n0 = x[0].strip('\'')
    n1 = x[1]
    n2 = x[2].strip(' \'')

    if len(x) != 3:
        raise NotImplementedError("Enter a convenient tuple.")
    if n0 == 'yes':
        if ( n1 < 29.5) :
            return 'less'
        else:
            return 'more'
    else:
        if n2 == 'good':
            return 'less'
        else:
            return 'more'
    # <<<<< END YOUR CODE


# In[48]:

x = ('yes', 32, 'good')
assert decision(x) == 'more'


# ## Reading a dataset from a text file (10 P)
# 
# The file `health-test.txt` contains several fictious records of personal data and habits.
# 
# * Read the file automatically using the methods introduced during the lecture.
# * Represent the dataset as a list of tuples.

# In[103]:


def gettest():
    # >>>>> YOUR CODE HERE
    with open('health-test.txt', 'r') as ftest:
        L = list()
        global count
        count = 0
        for line in ftest:
            print line
            count += 1 
            L.extend([x for x in str.split(line[:-1], ',')])
    print "number of lists:", count
    print L
    global subList
    subList = tuple([L[n:n+3] for n in range(0, len(L), 3)])
    print 'exp:', subList[5]
    print 'res:', decision(subList[5])
    
    if ftest == 0:
        raise NotImplementedError("Could not open file to read.")
    # <<<<< END YOUR CODE


# In[113]:

gettest()


# ## Applying the decision tree to the dataset (15 P)
# 
# * Apply the decision tree to all points in the dataset, and return the percentage of them that are classified as "more".

# In[179]:

def evaluate_testset():
    # >>>>> YOUR CODE HERE
    mores = 0
    for i in range(count):
        print decision(subList[i])
        if decision(subList[i])== 'more':
            mores = mores + 1
        if len(subList[i]) != 3:
            raise NotImplementedError("Given data is not convenient.")
     
    print "Health risk for the given dataset:%{}" .format((mores * 100)/count)
    
    
    # <<<<< END YOUR CODE


# In[180]:

evaluate_testset()


# ## Learning from examples (10 P)
# 
# Suppose that instead of relying on a fixed decision tree, we would like to use a data-driven approach where data points are classified based on a set of training observations manually labeled by experts. Such labeled dataset is available in the file `health-train.txt`. The first three columns have the same meaning than for `health-test.txt`, and the last column corresponds to the labels.
# 
# * Write a procedure that reads this file and converts it into a list of pairs. The first element of each pair is a triplet of attributes, and the second element is the label.

# In[256]:

def gettrain():
    # >>>>> YOUR CODE HERE
    with open('health-train.txt', 'r') as ftrain:
        
        T = list()
        line_counter = 0
        
        for line in ftrain:
            print line
            line_counter = line_counter +1
            T.extend([x for x in str.split(line[:-1], ',')])
            
        dataList = list()
        labelList = list()
        
        for i in range(line_counter * 4):
            if (i+1)%4 ==0:
                labelList.append(T[i])
            else:
                dataList.append(T[i])
        
        print 'dataList:{}\n'.format(dataList)
        print 'labelList:{}' .format(labelList)
        
        
        
            
        if ftrain == 0:
            raise NotImplementedError("Inconvenient type of data")
    # <<<<< END YOUR CODE


# In[257]:

gettrain()


# ## Nearest neighbor classifier (25 P)
# 
# We consider the nearest neighbor algorithm that classifies test points following the label of the nearest neighbor in the training data. For this, we need to define a distance function between data points. We define it to be
# 
# `d(a, b) = (a[0] != b[0]) + ((a[1] - b[1]) / 50.0) ** 2 + (a[2] != b[2])`
# 
# where `a` and `b` are two tuples corrsponding to the attributes of two data points.
# 
# * Write a function that retrieves for a test point the nearest neighbor in the training set, and classifies the test point accordingly.
# * Test your function on the tuple `('yes', 31, 'good')`

# In[ ]:

def neighbor(x, trainset):
    # >>>>> YOUR CODE HERE
    raise NotImplementedError("Replace this line by your code.")
    # <<<<< END YOUR CODE


# In[ ]:

# Test
x = ('yes', 31, 'good')
assert neighbor(x, gettrain()) == "more"


# * Apply both the decision tree and nearest neighbor classifiers on the test set, and find the data point(s) for which the two classifiers disagree, and with which probability it happens.

# In[ ]:

def compare():
    # >>>>> YOUR CODE HERE
    raise NotImplementedError("Replace this line by your code.")
    # <<<<< END YOUR CODE
    return Xdisagree, probability


# In[ ]:

Xdisagree, probability = compare()
assert type(Xdisagree) == list
assert probability >= 0.0 and probability <= 1.0


# One problem of simple nearest neighbors is that one needs to compare the point to predict to all data points in the training set. This can be slow for datasets of thousands of points or more. Alternatively, some classifiers train a model first, and then use it to classify the data.
# 
# ## Nearest mean classifier (25 P)
# 
# We consider one such trainable model, which operates in two steps:
# 
# (1) Compute the average point for each class, (2) classify new points to be of the class whose average point is nearest to the point to predict.
# 
# For this classifier, we convert the attributes smoker and diet to real values (for smoker: yes=1.0 and no=0.0, and for diet: good=0.0 and poor=1.0), and use the modified distance function:
# 
# `d(a,b) = (a[0] - b[0]) ** 2 + ((a[1] - b[1]) / 50.0) ** 2 + (a[2] - b[2]) ** 2`
# 
# We adopt an object-oriented approach for building this classifier.
# 
# * Implement the methods `train` and `predict` of the class `NearestMeanClassifier`.

# In[ ]:

class NearestMeanClassifier:
    def train(self, dataset):
        # >>>>> YOUR CODE HERE
        raise NotImplementedError("Replace this line by your code.")
        # <<<<< END YOUR CODE

    def predict(self, x):
        # >>>>> YOUR CODE HERE
        raise NotImplementedError("Replace this line by your code.")
        # <<<<< END YOUR CODE
        return prediction


# * Build an object of class `NearestMeanClassifier`, train it on the training data, and print the mean vector for each class.

# In[ ]:

def build_and_train():
    # >>>>> YOUR CODE HERE
    raise NotImplementedError("Replace this line by your code.")
    # <<<<< END YOUR CODE
build_and_train()


# In[ ]:




# * Predict the test data using the nearest mean classifier and print all test examples for which all three classifiers (decision tree, nearest neighbor and nearest mean) agree.

# In[ ]:

def predict_test():
    # >>>>> YOUR CODE HERE
    raise NotImplementedError("Replace this line by your code.")
    # <<<<< END YOUR CODE
    return agreed_samples
predict_test()


# In[ ]:



