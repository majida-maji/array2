rows=int(input("enter the no of rows:"))
for i in range(rows):
    for j in range(i):
        print(" ",end="")
    for j in range(rows,i,-1):
        print("*",end="")
    print()