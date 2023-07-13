list=[]
n=int(input("enter the no of elements:"))
for i in range(0,n):
    elements=[input(),int(input())]
    list.append(elements)
print(list)

large=list[0]
for i in range(len(list)):
    if list[i] >large:
        large=list[i]
        print(large)