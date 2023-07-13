rows=int(input("enter the no of rows:"))
for i in range(rows):
    for j in range(1,rows-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()