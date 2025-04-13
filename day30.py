# Method Overriding
# It allows a subclass to provide a specific implementation for a method already defined in its superclass

'''
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

rec = Shape(3,5)
print(rec.area)
'''


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class Circle(Shape): 
        def __init__(self, radius):
            self.radius = radius
            return super().__init__(radius, radius)

        def area(self):
            return 3.14 * super().area()

rec = Shape(3,5)
print(rec.area)

c = Circle(5)
print(c.area())