# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
sen=input("enter the sentence : ")
upper=0
lower=0
for i in sen:
    if(i.isupper()):
        upper=upper+1
    elif(i.islower()):
        lower=lower+1
print("no of upper case :",upper)
print("no of lower case :",lower)