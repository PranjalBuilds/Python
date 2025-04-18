#Operator overloading

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f'{self.i}i + {self.j}j + {self.k}k'
    
    def __add__(self, x):
        # return f'{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k'
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)

v = Vector(3,5,6)
print(v)

v2 = Vector(1,5,6)
print(v2)

print(type(v + v2))

