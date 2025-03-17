'''
Access modifiers in Python:
    Access modifiers in Python control the visibility of class attributes and methods

1. Public: Accessible from anywhere
2. Protected: Accessible only within the class and its subclasses
3. Private: Accessible only within the class

'''

# Public access modifier
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Person("Alice", 30)
print(a.name, a.age)

# Private access modifier

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

a = Person("Alice", 30)
#print(a.__name) # Can't be accessed
print(a._Person__name, a._Person__age) # Name mangling

''' 
    Name mangling :
        it changes private variables (__name) to _ClassName__name to avoid conflicts and accidental access. 
'''

# Protected access modifier

class Test:
    def __init__(self):
        self._protected = 42 

obj = Test()
print(obj._protected)  # Can be accessed