# dictionaries
# it's used to store data values in key:value pairs.

# it is a collection which is ordered, changeable and do not allow duplicates.

#example

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#accessing value from dictionary
print(thisdict["brand"])
print(thisdict.get("brand"))


print(thisdict["brand123"]) # returns err
print(thisdict.get("brand123")) # returns 'none'



#to print all keys of dictionary
print(thisdict.keys())

#iterating keys from dictionary
for key in thisdict:
    print(key) # prints keys of dictionary

# to print values 
print(thisdict.values())

#iterating values

for key in thisdict.keys():
    print(f"Keys: {key}\nvalues: {thisdict[key]}\n")



# key-value pairs:
print(thisdict.items())


for key, value in thisdict.items():
    print(f"Keys: {key}\nvalues: {value}\n")