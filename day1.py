#Day 1

print("Hello World");

#Escape Sequence Characters
print('Hey I am \"Pranjal Thakkar\" and I am learning Python');

#Separator
print('Hey','I','am','Pranjal','Thakkar',sep=' ~ ');

#Operators
#Arithmatic Operators
# + - * / // % **

#addition
result = 5 + 5
print(result)

#subtraction
result = 5 - 5
print(result)

#multiplication
result = 5 * 5
print(result)

#division
result = 5 / 5
print(result)

#floor division
result = 17 // 4
print(result)

#modulus
result = 17 % 4
print(result)

#exponentiation
result = 5**5
print(result)

#Comparison Operators
# < > <= >= == !=

#equal to
a = 5
b = 5
result = a == b
print(result)

#not equal to

a = 5
b = 5
result = a != b
print(result)

#greater than
a = 5
b = 10
result = b > a
print(result)

#less than

a = 4
b = 1
result = a < b
print(result)

#greater than or equal to

a = 43
b = 43
result = a >= b
print(result)

#less than or equal to

a = 19
b = 31
result = a <= b
print(result)

#LOGICAL OPERATORS

#and
p = True
q = False
result = p and q
print(result)

p = 5
q = 10
result = (p < 6) and (q > 8)
print(result)

#or
p = True
q = False
result = p or q
print(result)

p = 5
q = 10
result = (p < 3) or (q > 8)
print(result)

#not

p = False
q = True
result = not p or not q  #true or false --> true
print(result)