#dictionary methods

ep1 = {
    1: 81,
    2: 55,
    3: 33,
    4: 89,
    5: 78
}

ep2 = {
    6: 35,
    7: 68,
    8: 61
}

# update()
ep1.update(ep2)
print(ep1)

# clear()
ep1.clear()
print(ep1)

# empty dictionary
emp = {}
print(emp)

# pop - pop out the given item
ep2.pop(6)
print(ep2)

# popitem - removes last item from dictionary
ep2.popitem()
print(ep2)