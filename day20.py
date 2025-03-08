# constructors
# - used to automatically initialize an object's attributes when it is created

# typs of constructors: 
# - default constructor (only 'self')
# - parameterized constructor (self, ...)

#basic method:

# class Person:
#     name = 'John'
#     occupation = 'Intern'
#     sal = 10000

#     def info(self):
#         print(f'{self.name} is an{self.occupation} and, their salary is {self.sal}.')

# a = Person()

# # a.name = 'Manish'
# # a.occupation = 'HR'
# # a.sal = 30000


# a.info()


#-------------------------------------------------------


#with constructors:


class Person:

    def __init__(self, n, o, s):
        # print('This is a constructor')
        self.name = n
        self.occupation = o
        self.sal = s


    def info(self):
        print(f'{self.name} is {self.occupation} and, their salary is {self.sal}.')

a = Person("Harry", "Manager", 50000)
b = Person("Manish", "HR", 30000)

a.info()
b.info()