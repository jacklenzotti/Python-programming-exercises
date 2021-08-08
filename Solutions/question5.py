'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
'''

class Person():

    def __init__(self, name, age, pet = 'goat'):
        self.name = name
        self.age = age
        self.pet = ''

    def __str__(self):
        return "My name is {} and I'm {} year(s) old and have a {}".format(self.name, self.age, self.pet)

    def getString(self):
        self.pet = input()

    def printString(self):
        print(self.pet.upper())

person1 = Person('Micahel', 32)
print(person1)
person1.getString()
person1.printString()
print(person1)