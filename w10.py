word=str(input("enter the word : "))
for i in  word:
    if i.startswith("p"):
        print("welcome")
        break
    else:
        print("no entry")
        break