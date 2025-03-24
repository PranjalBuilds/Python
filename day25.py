# Static methods can be called directly - without creating an instance of the class first.

# in static method we don't have to use 'self', we should only have to use '@staticmethod' while declaration


class Math:
    def __init__(self, num):
        self.num = num 

    def addNum(self, n):
        self.num = self.num + n
    
    @staticmethod
    def add(a, b):
        return a + b

# rslt = Math(5)
# print(rslt.num)

a = Math(5)
print(a.add(5,1))
print(Math.add(5,1))