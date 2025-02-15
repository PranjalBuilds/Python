
# def double(x):
#     return x*2

# Lamda Function
    # A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

double = lambda x: x*2
cube = lambda x: x**x #cube of x

avg = lambda x,y :(x +y)/2
# avg = lambda x,y,z :(x + y + z) / 3

#print(cube(2))



def apply(func, val):
    return 6 + func(val)

#print(apply(cube,2)) # 6 + cube of 2



# anonymously
    # - it means to use function without defining it. for ex., here we didn't make any square function, but in apply(), it's being passed as square function

print(apply(lambda x : x*x, 12)) # 6 + square of 2