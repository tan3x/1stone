import random

class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self):
	time = '6:30'
	print(self.time)

clock = Clock('11:12')
clock.time = '11:11'
clock.print_time()


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

#Add the appropriate method(s) so that len(s) returns the number of elements in s.
    def getLen(self):
        return len(self)

#Define an intersect method that returns a new intSet containing elements that appear in both sets. In other words,
    def intersect(self, other):
        '''
        returns a new intSet whish has common elements in both sets
        '''
        intersect_set = intSet()

        for i in other.vals:
            if self.member(i):
                intersect_set.insert(i)

        return intersect_set

    def __len__(self):
        print  len(self.vals)
        return len(self.vals)

s1 = intSet()
s2 = intSet()

s1.insert(3)
s1.insert(5)
s1.insert(7)
s2.insert(3)
s2.__len__()

intSet.intersect(s1,s2)


#s1.intersect(s2) #same as below
#intSet.intersect(s1,s2)

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def getAge(self):
        return self.age
    def getName(self):
        return self.name
    def setAge(self, newAge):
        self.age = newAge
    def setName(self, newName):
        self.name = newName
    def __str__(self):
        return "Animal:" +str(self.name)+"Age:"+str(self.age)




class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:"+str(self.name)+"Age:"+self.age

class Human(Animal):
    def __init__(self, age, name):
        self.name = name
        self.age  = age
    def setName(self,name):
        self.name = name
    def setAge(self, age):
        self.age = age

    def compareAge(self, other):
        sAge = self.getAge()
        oAge =  other.getAge()
        if sAge > oAge:
            return True

class Student(Human):
    def __init__(self, name, age, major=None):
        Human.__init__(self, age, name)
        self.major = major
    def change_major(self,major):
        self = major
    def speak(self):
        r = random.random()
        if r < 0.25: print 'hw'
        elif 0.25<r<0.5: print 'eat'
        elif 0.5<r<0.75: print 'work'
        else : print 'sleep'


kater = Cat(Animal(12))
katze = Cat(Animal(5))
kater.setName('boncuk')
kater.speak()
Dog = Animal(12)
Dog.setName('yaman')

h1 = Human(12, 'human1')
h2 = Human(11, 'human2')
print h1.compareAge(h2)

s1 = Student('s1', 20, 'CE')

print s1












