# Multiple Inheritance
# When a class inherits features (methods and properties) from more than one parent class.

class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"name is : {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"Dance is : {self.dance}")


class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        self.name = name
        self.dance = dance

obj = DancerEmployee("Kathak", "Pooja")

print(obj.name)
print(obj.dance)

# when
# class DancerEmployee(Employee, Dancer):
obj.show() # name is : Pooja 

# when 
# class DancerEmployee(Dancer, Employee):
obj.show() # dance is : kathak 



 
# M.R.O. -- Method Resolution Order
# The order in which Python looks for a method or attribute when there are multiple parent classes.

print(DancerEmployee.mro())