# 'Super' keyword

'''
    It's a built-in function that provides access to methods and properties of a parent or superclass from a child or subclass, facilitating inheritance and allowing subclasses to extend or override parent class functionality.
'''



# Example 1:
# accessing parent class's method



'''
class GreatGrandpa:

    def greatGrandParentMethod(self):
        print("Hello, Great-Grandpa calling!")

class GrandpaFamily(GreatGrandpa):

    def grandParentMethod(self):
        super().greatGrandParentMethod() 
        print("Hello Grandpa Callin'!")

    def daddyMethod(self):
        print("What's up son, Daddy's here!")

    def sonMethod(self):
        print("Hello, Ancestors!")

childObj = GrandpaFamily()
childObj.grandParentMethod()

'''




# Example 2:
# accessing constructor of parent class



class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id  = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id) 
        self.lang = lang

John = Employee("John Doe", "E3010")
William = Programmer("William Murphy", "P1202", "Java")

print(f"\nName: {John.name}, id: {John.id}")
print(f"Name: {William.name}, id: {William.id}, Language: {William.lang}\n")