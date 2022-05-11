class Calculator:
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def Addition(self):
        print(self.a+self.b)
    def Subtraction(self):
        print(self.a-self.b)
    def Multiplication(self):
        print(self.a*self.b)
    def Division(self):
        print(self.a/self.b)
x=int(input("Enter First Number "))
y=int(input("Enter Second Number "))
c=Calculator(x,y)
print("Select the operation to be performed:")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
choice=int(input("Choose your operation: "))
if choice==1:
    c.Addition()
elif choice==2:
    c.Subtraction()
elif choice==3:
    c.Multiplication()
elif choice==4:
    c.Division()
else:
    print("Please Enter a Valid Choice")