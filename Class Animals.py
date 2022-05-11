class Animals:
    def speak(self):
        print("speaking")
class Dog(Animals):
    def speak(self):
        print("Whining")
class DogChild(Dog):
    def speak(self):
        print("Barking")
op=DogChild()
op.speak()