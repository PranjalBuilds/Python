# Function Cashing

'''
 It is an optimization technique that stores the results of 
 expensive function calls and returns the cached result when 
 the same inputs occur again. This avoids redundant computations 
 and significantly improves performance, 
 especially for functions that are called frequently with the 
 same arguments or involve I/O operations.

'''
# lru_cache

'''
 lru_cache is a decorator in Python's functools module that implements
 a Least Recently Used (LRU) caching strategy. 
 It is used to optimize the performance of functions by 
 storing the results of expensive function calls
 and returning the cached result when the same inputs occur again.
 ''' 

import functools
import time
import math

@functools.lru_cache(maxsize=None)

def fx(n):
    time.sleep(3)
    return (f"Factorial of {n} is : {math.factorial(n)}")
    
# takes 3 sec. to run
print(fx(2))
print(fx(3))
print(fx(4))

# gives output quickly      
print(fx(2))
print(fx(3))
print(fx(4))

# takes time for new value
print(fx(12))