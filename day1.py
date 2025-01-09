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


#ASSIGNMENT =
a = 5

#addition
a = 5
a += 2
print(a)

#subtraction
a = 5
a -= 2
print(a)

#multiplication
a = 10
a *= 3
print(a)

#division
a = 10
a /= 2
print(a)

#floor division
a = 15
a //= 4
print(a)

#modulus

a = 17
a %= 5
print(a)

#exponentiation
a = 2
a **= 3
print(a)


# MEMBERSHIP

#in

a = [1, 2, 3, 4, 5]
val = 3
#checks does values exists in the list
result = val in a
print(a)

#not in
a = "Hello, Pranjal!"
val = "Jainil"
result = val not in a
print(result)

# IDENTITY

#is
a = [1, 2, 3, 4, 5]
b = a
result = a is b
print(result)

#is not

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
result = a is not b
print(result)



#Precedence (High to low)


'''

#those who have same precedence are evaluated from left to right

Parentheses ()
Exponentiation ** 
Unary plus, unary minus, and bitwise NOT +x, -x, ~x
Multiplication, division, floor division, and modulus * / // %
Addition and subtraction + -
Bitwise left and right shifts << >>
Bitwise AND &
Bitwise XOR ^
Bitwise OR |
Comparisons, identity, and membership operators ==  !=  >  >=  <  <=  is  is not  in  not in
Logical NOT         not
Logical AND         and
Logical OR          or
'''
print(5 + 4 - 7 + 3)
#output: 5