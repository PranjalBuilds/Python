
# seek (), tell () and truncate()

with open('temp.txt', 'r+') as f: # r+    = read and write both
  txt = f.seek(3)       # starts operation after given number
  print(f.readline())   # reads the output of previous operation
  print(f.tell())       # tells us till where the seek operation performed 
  print(f.truncate(5))  # eliminates value from file according to given number 