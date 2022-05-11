class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=parrot("blu",10)
eagly=parrot("eagly",5)
print("Blu is a {}".format(blu.__class__.species))
print("Eagly is a {}".format(eagly.__class__.species))
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( eagly.name, eagly.age))