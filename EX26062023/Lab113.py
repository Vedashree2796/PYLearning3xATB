class Dog:
    name = None
    id = None

    def __init__(self):
        print("Default No Argument")

    def __init__(self, name=None, id=None): #constuctor has init
        self.name = name
        self.id = id

    def sleep(self): #function as normal name
        print("sleeping")


dog1 = Dog("Chow","1")
dog2 = Dog()
print(dog1.name)
print(dog1.id)