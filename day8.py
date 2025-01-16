# f-string

# without f-strings 
name = "Pranjal"
country = "India"

sentence = 'Hello! My name is {} and, I am from {}'
print(sentence.format(name, country))

#with f-string
print(f"Hello there! I'm {name} and, I'm from {country}")


#DocString - it is declared just before the code definition and used to describe about function

def add():
    '''This function adds two numbers and returns the result.'''
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    c = a + b
    print("Addition is:",c)

add()
print(add.__doc__)


#Recursion - Calling function within itself

#For Example: 
# factorial(n) : n * factorial(n-1)
# factorial(5) : 5 * factorial(4)
# factorial(4) : 4 * factorial(3)
# factorial(3) : 3 * factorial(2)
# factorial(2) : 2 * factorial(1)
# factorial(1) : 1 * factorial(0)  here, factorial(0) = 1

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(3))
print(fact(4))

# Fibonacci

# (i)
# 0 1 1 2 3 5 8 13 21 ...
# a b c

# (ii)
# c = a + b

# (iii)
# a = b
# b = c

# (iv)
# 0 1 1 2 3 5 8 13 21 ...
#   a b c


def fib(n):
    a = 0
    b = 1

    if n == 1: 
        print(a)
    elif n < 0:
        print("Invalid input")
    else:
        print(a)
        print(b)

        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)
fib(10) 