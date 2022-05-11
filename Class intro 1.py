class parrot:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        return "{} sings {}".format(self.name, song)
    def dance(self):
        return "{} is now dancing".format(self.name)
    def age(self):
        return 'age is {}'.format(self.age)
blu=parrot("Blu",10)
print(blu.sing("Happy"))
print(blu.dance())
print("Age is",blu.age)
zoro=parrot("Zoro",8)
print(zoro.sing("Enemy"))
print(zoro.dance())
print("Age is",zoro.age)