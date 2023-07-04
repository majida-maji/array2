# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
#
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

netamount=0
while True:
    s=input("enter the amount : ")
    if not s:
        break
    value=s.split(" ")
    op=value[0]
    amount=int(value[1])
    if op=="D":
       netamount+=amount
    elif op=="W":
        netamount-=amount
    else:
        pass
print("balance=",netamount)