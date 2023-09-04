salary=int (input("Sal :"))
age=int (input("Age :"))
if (salary>20000 or age<=30):
    loan=int (input("loan value : "))
    if (loan<50000):
        print("You will get")
    else:
        print("you are not eligible")
else:
    print("get out")