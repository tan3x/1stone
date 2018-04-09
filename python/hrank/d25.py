class Person(object):
	"""docstring for Person"""
	
	def __init__(self, name):
		self.name = name
	
	def revealIdentity(self):
		print "my name is {}" .format(self.name)

class SuperHero(Person):
	"""docstring for SuperHero"""
	
	def __init__(self, name, heroName):
		super(SuperHero, self).__init__()
		self.heroName = heroName

	def revealIdentity(self):
		print ".. and i am {}" .format(self.heroName)
		
		