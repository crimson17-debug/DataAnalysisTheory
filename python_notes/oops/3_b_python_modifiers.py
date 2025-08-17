class User:
    def __init__(self,username, email, password):
        self.username = username
        self._email = email         #intended to use only inside the class notthe outside the classs
        self.password = password


    @property
    def email(self):
        print("email is accesed")
        return self._email    #getter property
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
       
    
    
user1 = User("navya", "navya@gmail.com", 21233)
print(user1.email)


# user1.email = "navya123gmail"
# print(user1.email)                 throws an error since there is no setter property for this class name

# after setter
user1.email = "nav"
print(user1.email)





# advantages 
# we are making hte useer to believe that he is accessing the actual value 
# if we removfe the property decorator and protection then it still work in the display