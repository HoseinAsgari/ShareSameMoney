import random

class Room():
	@property
	def People(self):
		return self.people
	@People.setter
	def People(self, inPeople):
		self.people = inPeople
	
	def __str__(self):
		for person in people:
			print(person.name + ': ' + str(person.money) + '$')

	def ShareMoneyRandomly(self):
		for i in range(0, int(len(self.people)-1)):
			person1 = random.choice(people)
			person2 = random.choice(people)
			value = random.randint(1, person1.money+1)
			if person1.money <= 0:
				if person1.money < 0:
					value = value + person1.money
				self.people.remove(person1)
			person1.money -= value
			person2.money += value

class Person():
	def __init__(self, inName, inMoney):
		self.name = inName
		self.money = inMoney
	@property
	def Name(self):
		return self.name
	@property
	def Money(self):
		return self.money
	@Money.setter
	def Money(self, inMoney):
		self.money = inMoney


room = Room()

people = [Person("Ali", 20000), Person('Mohammad', 15000), Person('Mahdi', 25000), Person('Hossein', 15000), Person('Hassan', 2000000)]

room.People = people

shareCount = int(input('Enter share count: '))
for i in range(0, shareCount):
	room.ShareMoneyRandomly()

print (room)
