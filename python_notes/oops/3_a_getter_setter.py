
from datetime import datetime

class User:
    def __init__(self,username, email, password):
        self.username = username
        self._email = email         #intended to use only inside the class notthe outside the classs
        self.password = password

    def get_email(self):

        print(f"the email is accessed at {datetime.now()}")
        return self._email
    
    def set_email(self,email):
        if "@" in email:
            self._email = email
            return self._email
        else:
            return "Error:Not a valid email!"
    

user1 = User("navya", "navyama@gmail.com", 21223)
print(user1.get_email())

# user1._email = 232211 this is not adviced since it is protect we have to access it through a method

print(user1.set_email("nav123mail.com"))
