c=50
while c>0:
    print("Amount Due:",c)
    s=int(input("Insert coin: "))
    if s==25 or s==5 or s==10:
        c=c-s
    else:
        print("Error - this coin type not accepted")
print("Change Owed",c*-1)
