# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:


sen=input("enter the sentence : ")
alpha=0
digit=0
for i in sen:
    if(i.isalpha()):
        alpha=alpha+1

    elif(i.isdigit()):
        digit=digit+1
print("no of alphabet is : ",alpha)
print("no of digits is : ",digit)