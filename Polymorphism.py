class parrot:
    def fly(self):
        print("Parrot can Fly")
    def swim(self):
        print("Parrot Can't Swim")
class penguin:
    def fly(self):
        print("penguins can't Fly")
    def swim(self):
        print("Penguins Can Swim")
def Fly_Test(Bird):
    Bird.fly()
def Swim_Test(Bird):
    Bird.swim()
f=parrot()
p=penguin()
Fly_Test(f)
Fly_Test(p)
Swim_Test(f)
Swim_Test(p)