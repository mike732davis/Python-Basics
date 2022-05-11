class Students:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def setName(self):
        return "Name: {}".format(self.name)
    def setAge(self):
        return "Age: {}".format(self.age)
    def setMarks(self):
        return "Marks: {}/500".format(self.marks)
    def Display(self):
        return ("{} is the name of the student\nMark of the student is {}/500\nStudent is {} years old".format(self.name,self.marks,self.age))
Mike=Students("Mike",22,465)
print(Mike.setName())
print(Mike.setAge())
print(Mike.setMarks())
print(Mike.Display())