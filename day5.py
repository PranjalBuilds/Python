#lists 

listEx = [1,6,3,-2,True,"Banana"]
# print(type(listEx))
# print(listEx)

# print(listEx[0])

#print(listEx[-3]) convert to positive index
print(listEx[len(listEx)-3])



#Check element in list 
if 6 in listEx: 
    print('Yes!')
else:
    print('no')


# if 'ana' in listEx[3]:
#     print('yes')
# else :
#     print('no')



print(listEx[1:-2])
print(listEx[1:2:2]) #jump


#list Comprehension

lst = [i for i in range(4)]
print(lst) # [0,1,2,3]

#lst = [i*i for i in range[4]]
#print(lst) # [0,1,4,9]

lst = [i for i in range(9) if i %2 == 0]
print(lst) 




#list methods

# append, sort, reverse, index, count, copy, 

l = [1,3,4,6,7,8,9,1,1]

l.append(2)
print(f"append: {l}")

l.sort()
print("Sort: ",l)

# l.sort(reverse = True)
# print("Reverse: ",l)

l.reverse()
print("Reverse: ",l)

l.count(1)
print("Count: ",l)

l.index(6)
print("index: ", l)


m = l
m[0] = 0
print(l)

# Output is changed, * if reference is changed then, original will also be changed. to avoid that... use copy() method of list

m = l.copy()
m[0] = 0
print(l)


#insert - inserts element in the list at specified index

l.insert(1,993)

#extends

n = [900,1000,1100]
l.extend(n)
print(l)

#concatenation

k = l + n
print(k)