'''
Inheritance
    it allows us to define a class that inherits all the methods and properties from another class.

Parent class 
    is the class being inherited from, also called base class.

Child class 
    is the class that inherits from another class, also called derived class.

Types of Inheritance

    Single Inheritance
    Multiple Inheritance
    Multilevel Inheritance
    Hierarchical Inheritance
    Hybrid Inheritance

'''

#Single inheritance

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f"Name: {self.id} is : {self.name}")

class Programmer(Employee):
    def display(self):
        print("The language is Python!")


a = Employee("John", 101)
a.display()

#Multiple inheritance

class Mother:
    def mother(self, mothername):
        self.mothername = mothername
        print(self.mothername)

class Father:
    def father(self, fathername):
        self.fathername = fathername
        print(self.fathername)
 
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
  
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()

#Multilevel inheritance

class GrandPa:
    def __init__(self):
        self.age = 100
 
class Parent(GrandPa):
    def __init__(self):
        self.name = "Geek"
        GrandPa.__init__(self)

class GrandChild(Parent):
    def __init__(self):
        self.hobby = "Gaming"
        Parent.__init__(self)
 
    def display(self):
        print("Grandpa:", self.age)
        print("Parent:", self.name)
        print("Grandchild:", self.hobby)
 
obj = GrandChild()
obj.display()

#Hierarchical inheritance

class Calculate:
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
    def division(self):
        print(self.a / self.b)
 
class Add(Calculate):
    def __init__(self, a, b):
        Calculate.__init__(self, a, b)
 
    def add(self):
        print("Addition:", self.a + self.b)
        Add.division(self)
 
class Subtract(Calculate):
    def __init__(self, a, b):
        Calculate.__init__(self, a, b)
 
    def subtract(self):
        print("Subtraction:", self.a - self.b)
        Subtract.division(self)
 
obj1 = Add(34, 98)
obj2 = Subtract(45, 67)
obj1.add()
obj2.subtract()

#Hybrid inheritance

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):  # Hybrid Inheritance (Multiple + Hierarchical)
    pass

d = D()
d.show()  # Resolves using Method Resolution Order (MRO)