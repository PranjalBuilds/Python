# Hybrid and Hierarchical Inheritance

# Hybrid Inheritance
# blend of multiple inheritance types.

class BaseClass:
    pass

class DerivedOne(BaseClass):
    pass

class DerivedTwo(BaseClass):
    pass

class DerivedThree(DerivedOne, DerivedTwo):
    pass



#Example:
# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Derived class 1
class Employee(Person):
    def work(self):
        print(f"{self.name} is doing general employee tasks.")

# Another base class
class Trainee:
    def attend_training(self):
        print("Attending training sessions.")

# Final derived class combining both
class Intern(Employee, Trainee):
    def get_stipend(self):
        print(f"{self.name} receives a stipend.")

# Usage
intern = Intern("Charlie")
intern.work()              # from Employee
intern.attend_training()   # from Trainee
intern.get_stipend()       # own method



# Hierarchical Inheritance
#  type of inheritance in which a single base class is inherited by multiple derived classes.

'''

                    BaseClass:
                       |
     ------------------------------------
     |                 |                |
   DerivedOne      DerivedTwo       DerivedThree   
     ------------------------------------
     |                 |                |
    
    Sub               Sub 
  derived           derived           -----
  one, two           Three

      
'''

class BaseClass:
    pass

class DerivedOne(BaseClass):
    pass


class SubDerivedOne(DerivedOne):
    pass
class SubDerivedTwo(DerivedOne):
    pass


class DerivedTwo(BaseClass):
    pass

class SubDerivedThree(DerivedTwo):
    pass


class DerivedThree(BaseClass):
    pass



# Example:
# Base class
class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} is working...")

# Derived class 1
class Developer(Employee):
    def write_code(self):
        print(f"{self.name} is writing code.")

# Derived class 2
class Manager(Employee):
    def conduct_meeting(self):
        print(f"{self.name} is conducting a meeting.")

# Usage
dev = Developer("Alice")
dev.work()
dev.write_code()

mgr = Manager("Bob")
mgr.work()
mgr.conduct_meeting()
