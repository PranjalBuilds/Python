# Class Methods:
'''

class Emp:
    company = "abc"

    def show(self):
        print(f" Name: {self.name}\n Company: {self.company} ")
    
    @classmethod # this will make 'cls' work as a class, not an instance. i.e, cls = Emp.company.
    
    def changeCompany(cls, newCompany): 
        cls.company = newCompany

e1 = Emp()
e1.name = "Pranjal"
e1.show()

e1.changeCompany("xyz")
e1.show()

print(f"Actual Company: {Emp.company}") 


# extracting correct data

class Emp:
    def __init__(self, name, salary):
        self.name = name
        self.sal = salary

# e = Emp("Pranjal", 12000)
# print(e.name)
# print(e.sal)

str = "Naman-12000"
e = Emp(str.split("-")[0], int(str.split("-")[1]))
print(e.name)
print(e.sal)

'''

# Class Methods as an Alternative Constructors
 
class Emp:
    def __init__(self, name, salary):
        self.name = name
        self.sal = salary
    
    @classmethod
    def fromStr(cls, str):
        return cls(str.split("-")[0], int(str.split("-")[1]))

str = "Naman-12000"
e = Emp.fromStr(str)
print(e.name)
print(e.sal)

