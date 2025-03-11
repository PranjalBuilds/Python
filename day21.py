#Decorators:

# *args, **kwargs - for unknown number of arguments
# *args, - takes arguments as tuple
# **kwargs - takes arguments as dictionary 

def greet(func):
    def newFunc(*args, **kwargs): 
        print('Greetings!')
        func(*args, **kwargs)
        print('thanks for using!')
    return newFunc

#@greet
def hw():
    print('Hello World!')

def sum(a, b):
    print(a + b)


# sum() -- for @greet
# greet(hw)() # -- without @greet
greet(sum)(2, 3) # -- without @greet, with arguments

