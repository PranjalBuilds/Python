# Exception Handling - as name mentions, used to handle errors and stops the process of terminating code execution.



try: 
    table = int(input("Enter the no. to print the table of it. "))
    
    for i in range(1,11):
        print(f"{int(table)} X {i} = {int(table) * i}")
except:
    print("Error occured!")


# ValueError, ZeroDivisionError, IndexError, TypeError, NameError, SyntaxError

try:
    # SyntaxError (Uncomment to see this error)
    # eval('x === 10')

    # NameError
    print(undefined_variable)

    # ZeroDivisionError
    result = 10 / 0

    # IndexError
    lst = [1, 2, 3]
    print(lst[5])

    # ValueError
    num = int("abc")

    # TypeError
    result = "2" + 2

except SyntaxError:
    print("SyntaxError: Invalid syntax!")
except NameError:
    print("NameError: Variable not defined!")
except ZeroDivisionError:
    print("ZeroDivisionError: Division by zero is not allowed!")
except IndexError:
    print("IndexError: List index out of range!")
except ValueError:
    print("ValueError: Invalid literal for int()!")
except TypeError:
    print("TypeError: Unsupported operand type!")
except Exception as e:
    print(f"Other Error: {e}")

