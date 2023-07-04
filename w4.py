num=int(input("enter the no:"))

for i in range(2,num):
    if(num%i==0):
        print("no is not a prime")
        break
    else:
        print("no is prime")
        break