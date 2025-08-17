# name = "danny"
# age = 28

# print(name.upper())
# print(type(age))

class Dog:
    def __init__(self, name , breed, owner):    #parameter can be int string or even objects
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("whoof whoof")


class Owner:
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact



owner1 = Owner("sally", "12-alley", "888-899") #an object inside the class
dog1 = Dog("bruce", "scottish terrain", owner1)    #obj creation
dog1.bark()        #method used

print(dog1.name)
print(dog1.breed)
print(dog1.owner.name)


# when u create an object throught the class we are instantiating the class to create the instance object 












