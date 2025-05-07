# Walrus operator

# assigns values to variables as part of a larger expression.

happy = False
print(happy)
print(happy:=True)

# in While loop

# numbers = [1,2,3,4,5]

# while(n := len(numbers) > 0):
#     print(numbers.pop())

# ex.2
# without walrus
 
# foods = list()

# while True: 
#     food = input("What food do you like? : ")
#     if food == 'quit':
#             break
# food.append()

# with walrus 

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)