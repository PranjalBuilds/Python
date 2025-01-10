table = int(input("Enter the number that you want to print table of it: "))
for flag in range(table):
    flag = 1
    while(flag <= 10):
        print(f"{table} * {flag} = {table*(flag)}")
        flag += 1
    break