# dir(), __dict__ and help



# dir() - 
# it's basically used for discovering, what do you want about object

# x = [1,3,4]
# print(dir(x))

# x = (1,2,3)
# print(dir(x))
    
# print(dir) # built in function


# __dict__()

'''
# it returns a dictionary 
representation of an obJect's attributes. It is a useful tool for introspection.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

temp = Person("John", 28)
print(temp.__dict__)


'''

• The help() function is used to get help documentation for an object, including a description of its attributes and methods.

Example:
'''
print(help(Person))
