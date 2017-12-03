'''
s = 'azcbobobegghakl'
pattern = 'bob'
count =0
flag=True
start=0
while flag:
    a = s.find(pattern,start)  # find() returns -1 if the word is not found,
                                  #start i the starting index from the search starts(default value is 0)
    if a==-1:          #if pattern not found set flag to False
        flag=False
    else:               # if word is found increase count and set starting index to a+1
        count+=1
        start=a+1
print(count)
'''

'''
s='abcdefefef'
sLongest = []
for i in range(len(s) - 1):
    if s[i] < s[i + 1]:
        sLongest.append(s[i])
    else:
        break


print('Longest substring in alphabetical order is: %s' % ''.join(sLongest))
'''

'''

lowend = 0
highend = 100
guess = 50
choice = 0

print ("Please think of a number between 0 and 100!")
print ("Is your secret number " + str(guess) + "?")
while choice != 'c':
    print("Enter 'h' to indicate the guess is too high. " + "Enter 'l' to indicate the guess is too low.")
    choice = raw_input("Enter 'c' to indicate I guessed correctly.")
    if choice == 'c':
        break
    elif choice == 'h':
            highend = guess
            guess = int((highend + lowend)/2)
            print ('Is your secret number ' + str(guess) + "?")
            choice = 0
    elif choice == 'l':
            lowend = guess
            guess = int((highend + lowend)/2)
            print ('Is your secret number ' + str(guess) + "?")
    else:
            print ("Sorry, I did not understand your input.")
            choice = 0

print ('Game over. Your number was: ' + str(guess) + ".")

'''

def iterPower(base, exp): #iterative: withloop
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    n=1
    result=1

    for n in range(n,exp+1):

        result = result*base

    return result

'''
def recurPower(base, exp): #recursive: calling function again

    if exp==1:
        return base
    elif exp==0:
        return 1
    elif exp!=1:
        return base* recurPower(base, exp-1)

print(recurPower(4,4))
'''
'''
def gcdIter(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
'''
'''
def gcdRecur(x,y):
    if y == 0:
        return x
    else:
        return gcdRecur(y, x % y)
print (gcdRecur(8,2))
'''

def isIn(char, aStr):
    '''
        char: a single character
        aStr: an alphabetized string

        returns: True if char is in aStr; False otherwise
        '''
'''
    if aStr == '' :  # Check for empty string
        return False
    s=sorted(aStr)
    m = aStr[len(s) // 2]
    if char == m:
        return True
    elif len(aStr) == 1:
        return False
    else:
        if char < m:
            return isIn(char, aStr[:len(aStr) // 2])
        elif char > m:
            return isIn(char, aStr[len(aStr) // 2:])
    return isitIn(char, aStr)
    
print(isIn('x', 'berlix'))
'''
'''
def polysum(n, s):
    
    #:param n: number of sides
    #:param s: lenth of one side
    #:return:
    
    import math as mathe
    nominator = (0.25 * n * s ** 2 )
    denominator =  mathe.tan((mathe.pi)/n)
    area = nominator/ denominator
    perimeter = s * n
    perimeter2 = perimeter ** 2
    sum = round((area + perimeter2),4)

    print ('Polysum function:%s' % str(sum))
    return sum

polysum(32,30)

'''


def calcBalance(debt, annualInterestRate, monthlyPaymentRate):
    '''
    :param debt: total debt
    :param annualInterestRate: annual interest rate as decimal
    :param monthlyPaymentRate: min monthly payment rate
    :return: balance: remaining balance with 2 decimals

    '''
    monthlyInterest = annualInterestRate / 12.0
    totalPayment  = 0
    i = 1

    while i < 12:
        monthlyPayment = debt * monthlyPaymentRate
        debt = debt - monthlyPayment
        mInterest = monthlyInterest * debt
        balance = debt + mInterest
        totalPayment += monthlyPayment

        i += 1

    print ('Remaining debt:%s' % str(balance))
    print ('Total Payment:%s' % str(totalPayment))

    return balance

calcBalance(42, 0.2, 0.04)

'''
def oddTuples(aTup):
    
    #aTup: a tuple

    #returns: tuple, every other element of aTup.
    
    # Your Code Here
    bTup = ()

    for i in range(0,len(aTup),1):
        if i % 2 == 0:
            bTup = bTup + (aTup[i],)
    return  bTup

print(oddTuples((1,2,3,4,5,'totemo','oishi')))
'''
'''
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    print 'Function applied to each:', str(L)

def times5(x):
    return x*5
def absolute(x):
    return abs(x)
def increment(x):
    return x+1
def square(x):
    return x**2

list = [1, -4, 8, -9]
applyToEach(list,square)

def applyEachTo(L,a):
    result=[]
    for i in range(len(L)):
        result.append(L[i](a))
    print 'Functions applied on variable', result
    return result

def absolut(x):
    return abs(x)
def incuat(x):
    return x+1
def squat(x):
    return x**2
def halve(x):
    return x/2

list2 = [absolut, incuat, squat, halve]
applyEachTo(list2, -3)

'''

