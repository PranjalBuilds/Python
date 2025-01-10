import time

# timeStamp = int(time.strftime('%d-%m-%y %H:%M:%S'))
# print(timeStamp)

print("****** Greetings!  ******")

hr = int(input("Enter the current hour: "))

if(hr >= 0 and hr < 12):
    print("Good Morning!")
elif(hr >= 12 and hr < 16):
    print("Good Afternoon!")
elif(hr >= 16 and hr < 20):
    print("Good Evening!")
elif(hr >= 20 and hr < 24):
    print("Good Night!")
else:
    print("Enter a valid number!")