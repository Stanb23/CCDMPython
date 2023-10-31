class OddEvenExceptions:
    pass 
try:
    userchoice=int(input("Enter Number"))
    if userchoice % 2 == 0:
        print(str(userchoice + "is an EVEN number"))

    else:
        print(str(userchoice + "is an ODD number"))

except userchoice:
    print("Sorry! but invalid integer value")

OddEvenExceptions()
