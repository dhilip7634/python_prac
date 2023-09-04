a=int (input("A :"))
b=int (input("B :"))
ope=input("add/multi/div/sub :")
if(ope=="add"):
    print(a+b)
elif(ope=="multi"):
    print(a*b)
elif(ope=="div"):
    print(a/b)
elif(ope=="sub"):
    print(a-b)
else:
    print("Invalid Option")