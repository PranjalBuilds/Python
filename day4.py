#functions arguments

'''

Default 
keyword
variable-length
required

'''

#default args.
def avg(a = 9, b = 3):
    print('The Average is : ', (a + b)/2)

avg()
# avg(1, 5)  -> will overwrite args
# avg(4)     -> will overwrite a's value
# avg(b = 4) -> will change b's value



#keyword args - order doesn't matter
def avg(a = 9, b = 3):
    print('The Average is : ', (a + b)/2)

avg(b = 9, a = 3) 


#variable length - we can pass n number of inputs in function while calling
# * tuples, ** - dictionary  
def avg(*numbers): 
    #print(type(numbers))
    sum = 0
    for i in numbers:
        sum += i
    print('Average is : ', sum/len(numbers))

avg(2,4,6,8,10)

# required args
def avg(a,b):
    print('The Average is : ', (a + b)/2)

avg(3,6)

