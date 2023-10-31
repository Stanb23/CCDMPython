class Cat():

  #Constructor
  Cat="Feline"
  def  init_(self,cname,color,weight,breed):
    self.cname=cname
    self.color=color
    self.weight=weight
    self.breed=breed

  def printcatsdetails(self):
    print("------Cat's details------")
    print("Name:  ",self.cname)
    print("Color:  ",self.color)
    print("weight:  ",self.weight, "in kg")
    print("breed:  ",self.breed)


usercname = str(input("Hi, please enter the following questions:\nCat's name?"))
usercolor = str(input("Cat's Color?"))
userweight = str(input("Cat's Weight in kg?"))
userbreed = str(input("Cat's breed?"))

#Rewrite the objects
mycat=Cat(usercname,usercolor,userweight,userbreed)

#Use Object



