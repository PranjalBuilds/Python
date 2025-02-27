# OOP in Python

# Class - it's a "blueprint" for creating objects.

# class MyClass:
#   x = 5

# p1 = MyClass()
# print(p1.x)

#-------------------------------------------------------

# class Person:
#   name = 'John'
#   occupation = 'Intern'
#   sal = 10000

# a = Person()
# print(a.name, a.occupation, a.sal)

# e = a.name = 'Manish'
# f = a.occupation = 'HR'
# g = a.sal = 30000

# print(e, f, g)


#-------------------------------------------------------

class Person:
  name = 'John'
  occupation = 'Intern'
  sal = 10000
  
  def info(self):
    print(f'{self.name} is {self.occupation}, their salary is {self.sal}.')

a = Person()
a.info()