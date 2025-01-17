# Set

# set is a collection of well-defined objects.
# in sets, there are only unique members.

setEx = {1,2,3,4,1,2}
print(setEx) # 1 2 3 4

a = {1,False,'John',19.4,-2}
print(a)

#empty set
b = set()

# Iterating data from set
for i in a:
    print(i)


# set operations

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = {10,12}

#union 
# a ∪ b
print("Union: ", s1.union(s2))


# update() - performs union and replaces s1 with s3 (below)
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = {10,12}
check = s1.update(s3)

print("update: ",check)

#difference between union() and and update()

cty1 = {'Delhi', 'Mumbai', 'Kolkata', 'Chennai'}
cty2 = {'Prayagraj', 'Kolkata', 'Chennai', 'Ahmedabad'}

result = cty1.union(cty2)
print("Union: ", result)

# cty1.update(cty2)
cty1 = {'Delhi', 'Mumbai', 'Kolkata', 'Chennai'}
cty2 = {'Prayagraj', 'Kolkata', 'Chennai', 'Ahmedabad'}
cty1.update(cty2)
print("update: ", cty1)

#intersection 
# a ∩ b
cty1 = {'Delhi', 'Mumbai', 'Kolkata', 'Chennai'}
cty2 = {'Prayagraj', 'Kolkata', 'Chennai', 'Ahmedabad'}
ctyIntersection = cty1.intersection(cty2)
print("Intersection: ", ctyIntersection)


#intersection update - performs intersection and replaces cty1 with cty2
cty1 = {'Delhi', 'Mumbai', 'Kolkata', 'Chennai'}
cty2 = {'Prayagraj', 'Kolkata', 'Chennai', 'Ahmedabad'}
cty1.intersection_update(cty2)
print("Intersection update: ", cty1)


#symetric difference 
# (a - b) ∪ (b - a)
# (a ∪ b) - (a ∩ b)
cty1 = {'Delhi', 'Mumbai', 'Kolkata', 'Chennai'}
cty2 = {'Prayagraj', 'Kolkata', 'Chennai', 'Ahmedabad'}
ctysd = cty1.symmetric_difference(cty2) # those elements which are not present in cty1 from cty2 and, in cty2 from cty1
print("Symetric diff: ", ctysd)


# difference 
# (a - b)
cty1 = {'Delhi', 'Mumbai', 'Kolkata', 'Chennai'}
cty2 = {'Prayagraj', 'Kolkata', 'Chennai', 'Ahmedabad'}
ctydf = cty1.difference(cty2) # elements that cty1 don't have from cty2
print("difference: ", ctydf)



# isdisjoint()
# returns true or false whether given sets are disjoint or not.
cty1 = {'Delhi', 'Mumbai', 'Kolkata', 'Chennai'}
cty2 = {'Prayagraj', 'Kolkata', 'Chennai', 'Ahmedabad'}
print("is disjoint: ", cty1.isdisjoint(cty2)) # false


#issuperset()
# shows if cty3s' elements are present in cty1 or not

cty1 = {'Delhi', 'Mumbai', 'Kolkata', 'Chennai'}
cty2 = {'Prayagraj', 'Kolkata', 'Chennai', 'Ahmedabad'}
cty3 = {"Kolkata", "Mumbai"}
ctysuper = cty1.issuperset(cty3)
print("issuperset: ", ctysuper)

#issubset()
# shows if cty3 has elements of cty1 or not

cty1 = {'Delhi', 'Mumbai', 'Kolkata', 'Chennai'}
cty2 = {'Prayagraj', 'Kolkata', 'Chennai', 'Ahmedabad'}
cty3 = {"Kolkata", "Mumbai"}

ctysub = cty3.issubset(cty1)
print("issubset: ", ctysub) # True


#add
cty1.add("Gurugram")
print("add: ",cty1)

# remove () / discard () - both removes elements

# difference

# remove - will throw err if element is not present 
# discard - will not throw err if element is not present and continue to the next line of code 

cty1 = {'Delhi', 'Mumbai', 'Kolkata', 'Chennai'}
cty2 = {'Prayagraj', 'Kolkata', 'Chennai', 'Ahmedabad'}
cty3 = {"Kolkata", "Mumbai"}

# cty1.remove("Gurugram") 
# print("remove: ",cty1)

cty1.discard("Gurugram") 
print("discard: ",cty1)


#pop
# removes one random element from set
 
popped = print(cty1.pop())
print("popped item: ", popped)


#del 
# used to delete entire set
cty1 = {'Delhi', 'Mumbai', 'Kolkata', 'Chennai'}
del cty1


#clear()
# delete all the items of the set 
cty2 = {'Delhi', 'Mumbai', 'Kolkata', 'Chennai'}
cty2.clear()