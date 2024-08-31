class Dog:
    name = None
    id = None

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def sleep(self):
        print("Who is Sleeping -> " + self.name)


dog1 = Dog("Chow", "1")
dog2 = Dog("Mow", "2")


print(f'{dog1.name} has ID {dog1.id}')
print(f'{dog2.name} has ID {dog2.id}')

dog1.sleep()
dog2.sleep()


#Object -> line 13&14
#Constructor -> Line5
#self -> Current object
#method -> line 5&9
# Instance variable 2&3
# constructor can not have return types
# we can have 2or more return type