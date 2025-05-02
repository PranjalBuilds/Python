# Multilevel Inheritance
# When a derived class is derived from another derived class, that's called multilevel inheritance

# Syntax:
class BaseClass:
    pass

class DerivedClass(BaseClass):
    pass

class SubderivedClass(DerivedClass):
    pass

# Example:

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self) #2
        print(f"Breed: {self.breed}") #3
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self) #1
        print(f"Color: {self.color}") #4

o = Dog("tommy", "Black")
o.show_details()
print(GoldenRetriever.mro())

# benefit of using multilevel inheritance is having reusability of code , reducing repeatability and redunduncy.

# we can easily excess previous / parent class properties very easily!