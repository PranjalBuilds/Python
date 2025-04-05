# Class Methods:

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