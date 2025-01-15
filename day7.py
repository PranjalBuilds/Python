#tuple operations


# tup = ('Spain', 'Germany', 'Italy', 'India', 'Russia', 'Nepal', 'Bhutan')

# temp = list(tup)
# temp.append('USA')

# temp.pop(1)

# temp[0] = 'Finland'

# tup = tuple(temp)
# print(tup)



# tuple concatenation
a = ('A', 'B', 'C', 'D')
b = ('E', 'F', 'G', 'H')

c = a + b
print(c)


# count, index, length

    #  0 1 2 3 4
num = (1,3,1,3,2)
print(num.count(2)) #count occurences of given input



print(num.index(2)) # gives the first occurence (index) of given input

print(num.index(3, 2, 4)) # gives the index occurence (index of original tuple) of 2 by printing index no. 2 to 4 (4 is not included) #output : 3



print(len(num)) # output: 5