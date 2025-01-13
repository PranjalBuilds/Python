#lists 

listEx = [1,6,3,-2,True,"Banana"]
# print(type(listEx))
# print(listEx)

# print(listEx[0])

#print(listEx[-3]) convert to positive index
print(listEx[len(listEx)-3])


''' 
#Check element in list 
if 6 in listEx: 
    print('Yes!')
else:
    print('no')


if 'ana' in listEx[3]:
    print('yes')
else :
    print('no')

'''

print(listEx[1:-2])
print(listEx[1:2:2]) #jump


#list Comprehension

lst = [i for i in range(4)]
print(lst) # [0,1,2,3]

#lst = [i*i for i in range[4]]
#print(lst) # [0,1,4,9]

lst = [i for i in range(9) if i %2 == 0]
print(lst) 