name=["athul","jithin","amal"]
pswd=["a123","b123","c123"]


for i in name:
    nm = str(input("enter your name:"))
    if(i!=nm):
        print(("incorrect name"))
        break
    for j in pswd:
        ps = str(input("enter your password"))
        if(j!=ps):
            print("incorrect password")

        if(i==nm and j==ps):
            print("welcome",nm)
            break



