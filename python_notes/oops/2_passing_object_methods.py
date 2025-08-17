##################how to use the properties like name and age inside the class ----self.property

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"hello there my name is {self.name} and my age is {self.age}")


person1 = Person("navya", 23) #instantiation
person1.greet()

person2 = Person("Maidhili", 12) #person1 and person2 are instances of person class
person2.greet()

################passing object in a method/####################
class User:
    def __init__(self,username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username}: HI {user.username} , its's {self.username}")


user1 = User("dantman", "dantgmail.com", 234)
# user2 = User("batman", "batmangmail.com", 2345)

# user1.say_hi_to_user(user2)


