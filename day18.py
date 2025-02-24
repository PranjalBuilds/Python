#difference between 'is' and '==' operator

'''
both are comparision operator but... 

'is' returns exact location in memory and,
'==' returns value

'''

a = 4
b = "4"

print(a is b) # false
print(a == b) # false

c = [1,3,4,5]
d = [1,3,4,5]

print(c is d) # false
print(c == d) # true

e = 1
f = 1

print(e is f) # true
print(e == f) # true

'''
 the same elements of same datatypes will always return true whether it's 

 None, String, number, tuples, etc.! 
'''