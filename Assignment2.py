class Triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def TriArea(self):
        print("Area is",self.base*self.height/2,"cm2")
  
                
    def Triperi(self):
      print("Perimeter is",self.base*3,"cm")

TriBase=int(input("Enter your base(cm)"))
TriHeight=int(input("Enter your height (cm)")) 

TriObject=Triangle(TriBase,TriHeight) 
Triobj=Triangle(TriBase,TriHeight)

TriObject.TriArea()
Triobj.Triperi()






