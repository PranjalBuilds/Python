import os
import sys 

b = int(input('Do you want to delete the file?\n1 to delete\n2 to keep\n'))

if b == 2:
    print('File will be kept!')
    sys.exit()

ls = os.listdir()

if b == 1:
    for fl in ls:
        print(f'{fl}\n') 
    c = input('Enter the file name: ').strip()
    
    if os.path.exists(c):
        os.remove(c)
        print('File deleted!')
    else:
        print('Error: File does not exist!')
else:
    print("Invalid option!")
    
