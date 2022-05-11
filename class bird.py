class bird:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        return "{} sings {}".format(self.name, song)
    def dance(self):
        return "{} is now dancing".format(self.name)
    def age(self):
        return 'age is {}'.format(self.age)
parrot=bird("Parrot",10)
print(parrot.sing("Happy"))
print(parrot.dance())
print("Age is",parrot.age)
eagle=bird("Eagle",8)
print(eagle.sing("Enemy"))
print(eagle.dance())
print("Age is",eagle.age)