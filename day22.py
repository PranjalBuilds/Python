#getters and setters

class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f'{self._value} is the value!')

    @property
    def newVal(self):
        return 10 * self._value

    @newVal.setter
    def newVal(self, new_value):
        self._name = new_value/10


obj = MyClass(10)
obj.newVal = 67
print(obj.newVal)
obj.show()  