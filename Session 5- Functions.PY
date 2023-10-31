#Distance Converter
#Create a distance converter which converts distance
#Function

def DistConverter():
    choice=int(input("Enter 1 for m to km \nEnter 2 for km to m\n"))
    if choice==1:
        dist=int(input("Enter distance in meters\n"))
        ans=dist/1000
        print("distance is:"+ str(ans) + "km")
    elif choice==2:
        dist2=int(input("Enter distance in kilometres\n"))
        ans2=dist2*1000
        print("distance is:"+ str(ans2) + "m")

    else:
        print("Sorry, wrong choice. Please select 1 or 2")

DistConverter()





    

       
   



#Call the function 
#DistConverter(500)

def nameage(name,age):
    print("Hi"+ name)
    print("Your age is:" + str(age))

    #Call this Function
#nameage("Stanoc", 22)

def calculation (a,b):
    ans=a+b
    print(ans)

#result=calculation(10,15)
#print=(result)
