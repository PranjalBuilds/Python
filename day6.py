t = (1,3,4,6,7)
print(type(t))

# t = (5) # int
# t = (5,) # 'tuple'
# print(type(t))

# t[0] = 90 #assigning new value to 0th index
# print(t[0]) # will throw err

#       * tuples can't be manipulated as lists
#       * tuples are immutable
#       * tuples are faster than lists
#       * tuples are more memory efficient than lists
#       * tuples are hashable, lists are not
#       * tuples can be used as dictionary keys, lists can't
#       * tuples can be used as set elements, lists can't
#       * tuples can be used as return values, lists can't
#       * tuples can be used as function return values, lists can't
#       * tuples can be used as function arguments, lists can't

tup = (1,3,4,True,-1,0)
print(type(tup),tup)

print(tup[0])
print(tup[1])
print(tup[2])

print(tup[-3]) # len(tup) - 3, 6 - 3 = 3, tup[3] = True



if 3 in tup:
    print('Yes, it is.') # True
else: 
    print("No it isn't")


if '3' in tup:
    print('Yes, it is.') 
else: 
    print("No it isn't") # True



print(tup[1:4]) # 3, 4, True
print(tup[:2])  # 0:2 -> 1,3
print(tup[0:])  # 0:len(tup) -> 1,3,4,True,-1,0



#mutable -> can be changed, ex. lists, sets, dictionaries..
#immutable -> can't be changed, ex.  strings, numbers, tuples ...

