# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
def ex():
    list=[]
    n=int(input("enter the range :" ))
    for i in range(0,n+1):
        if(i%5==0 and i%7==0):
            list.append(str(i))
    print(",".join(list))
ex()