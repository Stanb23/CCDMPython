#Exercise 1
#Question 1: Create a variable that holds the string hello
x ="hello"
print(x +" " +"Stanoc Baim")

#Question 2: 
print(x[0])
print(x[1])

#Question 3:
x="hello world"
s=x[0:3]
print(s)
s=x[:3]
print(s)

#Question 4:
myname="Stanoc Baim"
print ( "Welcome" + " " +  myname  + " " + "to CCDM Course")
 

#Session2
#Create Python Lists and Access Python List Elements
Courses= ["CCIT","CCDM","CCNS","CCLSA"]
print(Courses)
print(Courses[2])

#Negative Indexing
print(Courses[-1])
print(Courses[-2])

#Slicing of a Python List
#List Slicing in Python
mylist= ['p','r','o','g','r','a','m','i','z']
#items from Index 2 - Index 4
print(mylist[2:5])
#items from Index 5 to End
print(mylist[5:])
#items from Beginning to End
print (mylist[:])

#Add Elements to a Python Lists
#Add Element #1: Append
Courses.append ("CCAIT")
print(Courses)

#Remove Elements from a Python List
del Courses[0]
print(Courses)

#Exercise 2
#Question 1A:Cities
Cities= ["New York","Los Angeles","Boston","Denver"]
print(Cities)
print(Cities[0])

#Question 1B:Numbers
Numbers=['1','3','4','6','4','7','8','2','3']
print(Numbers)
print(sum(Numbers))
print(min(Numbers))
print(Numbers(0))
print(Numbers[-1])
