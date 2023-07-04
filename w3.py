first=[]

for i in range(1,101):
    if(i%12==0):
       first.append(i)

print(first)
second=[]
for j in first:
    if(j%14==0):
        second.append(j)
print(second)