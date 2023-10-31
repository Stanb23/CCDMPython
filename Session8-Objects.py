class Rectangle:
    #Create Constructor
     def __init__(self,length,width):
            self.length = length
            self.width = width

     def RectArea(self):
             print("Area is",self.length*self.width,"cm2")

userlength = int(input("Enter Length (cm)"))
userwidth = int(input("Enter Width (cm)"))

#Object Instantation - Attach to class only with parameters
rectObject = Rectangle(userlength,userwidth)

#Use the Object
#rectObject.RectArea()


class Perimeter:
    def __init__(self,sidelength,sidewidth):
                self.sidelength=sidelength
                self.sidewidth=sidewidth
        
    def RectPeri(self):
        print("Area is",2*self.sidelength+2*self.sidewidth,"cm")

Perilength=int(input("Enter Length (cm)"))
Periwidth=int(input("Enter Width (cm)"))

Periobj= Perimeter(Perilength,Periwidth)

Periobj.RectPeri()
