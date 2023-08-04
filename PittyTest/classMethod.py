# Python program to demonstrate
# use of a class method and static method.
from datetime import date

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# a class method to create a
	# Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	def display(self):
		print("Name : ", self.name, "Age : ", self.age)

person = Person('mayank', 21)
person.display()
print(Person.fromBirthYear('phu', 2023))
