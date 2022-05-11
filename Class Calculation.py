class Calculation1:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def summation(self):
        print("summation is",self.x+self.y)
class Calculation2:
    def multiplication(self):
        print("multiplication is",self.x*self.y)
class Calculation3(Calculation1,Calculation2):
    def division(self):
        print("division is",self.x/self.y)
a=int(input("Enter the number "))
b=int(input("Enter the number "))
C=Calculation3(a,b)
C.summation()
C.multiplication()
C.division()