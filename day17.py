# Map, Filter and Reduce

#Map: 


# Suppose, we want a cube of each number in this list, how we traditionally approach:

def cube(x):
    return x ** x
 
l = [1,2,3,4,5,6,7]
newL = []

for item in l:
    # print(cube(item))
    newL.append(cube(item))

print(newL)

# Instead of this we can use 'map'
# print(map(cube, l)) # returns map obj.

newL = list(map(cube, l))
print(newL)



# Filter

# To filter a list in Python, we can use filter() function along with a lambda function or a defined function.

def filter_Func(a):
    return a > 4

newnewL = list(filter(filter_Func, l))
print(newnewL)


# Reduce
# The reduce function is used to apply a function of two arguments cumulatively to the items of a list (or any iterable), from left to right

from functools import reduce

abc = [1,2,3,4,5] # 1 + 2 = 3, 3 + 3 = 6, 6 + 4 = 10, 10 + 5 = 15

def mySum(a,b):
    return a + b

sum = reduce(mySum, abc)
print(sum)