# Exception Handling - as name mentions, used to handle errors and stops the process of terminating code execution.



# try: 
#     table = int(input("Enter the no. to print the table of it. "))
    
#     for i in range(1,11):
#         print(f"{int(table)} X {i} = {int(table) * i}")
# except:
#     print("Error occured!")


# # ValueError, ZeroDivisionError, IndexError, TypeError, NameError, SyntaxError

# try:
#     # SyntaxError (Uncomment to see this error)
#     # eval('x === 10')

#     # NameError
#     #print(undefined_variable)

#     # ZeroDivisionError
#     result = 10 / 0

#     # IndexError
#     lst = [1, 2, 3]
#     print(lst[5])

#     # ValueError
#     num = int("abc")

#     # TypeError
#     result = "2" + 2

# except SyntaxError:
#     print("SyntaxError: Invalid syntax!")
# except NameError:
#     print("NameError: Variable not defined!")
# except ZeroDivisionError:
#     print("ZeroDivisionError: Division by zero is not allowed!")
# except IndexError:
#     print("IndexError: List index out of range!")
# except ValueError:
#     print("ValueError: Invalid literal for int()!")
# except TypeError:
#     print("TypeError: Unsupported operand type!")
# except Exception as e:
#     print(f"Other Error: {e}")



# #finally - this clause will always execute without taking care of try and except block.

# try:
#     a = 1
#     if a > 2:
#         print(" > 2 ")
#     else: 
#         print(" < 2 ")

# except Exception as e:
#     print(e)

# finally: 
#     print("This will Always be executed!")


# the difference between normal print statement in outer block and finally clause is, print won't execute when function is called but, finally will, regardless of any interuptions or terminations




# raise 
# raises custom exceptions


a = input("Enter the value between 5 and 9 press 'Q' to quit : ").lower()

if(a == "q"):
    print("Thank You")
elif(int(a)<5 or int(a)>9):
    raise ValueError("The given item is invalid")