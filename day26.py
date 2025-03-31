class Employee:
    companyName = "xyz" # class variable
    noOfEmp = 0

    def __init__(self,name):
        self.name = name # instance variable
        self.salary = 75000
        Employee.noOfEmp += 1

    def showDetails(self):
        print(f" \n Employee name: {self.name}\n Company: {self.companyName}\n salary:{self.salary}\n Total Employees: {self.noOfEmp}\n")



emp1 = Employee("John")
emp1.companyName = 'abc' #output : abc
emp1.showDetails()
#Employee.showDetails(emp) # we can also do this!

emp2 = Employee("Maven")
emp2.salary = 80000
emp2.companyName = 'pqr' # this will create a instance variable named companyName for Maven
emp2.showDetails()


# Python replaces the companyName even after it is not a instance variable because, 
# it checks if this instance belongs to a instance varible or not, if not then it goes for class variable, if it gets the same named variable from class then it performs the action