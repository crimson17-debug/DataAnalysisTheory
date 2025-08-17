#accesing and modifying data:
#the java traditional way getter and seteters

class User:
    def __init__(self,username, email, password):
        self.username = username
        self._email = email         #intended to use only inside the class notthe outside the classs
        self.password = password
    
    def get_emai(self):
        return self._email
    
    def clean_email(self):
        return self._email.lower().strip() #strip is used to remove white spaces
    
user1 = User("nanni", "NaNN ni@gmail.com", 12321)

# print(user1._email)     #programmers are not supposed to use it outside the class as it is intended to use it outside

print(user1._email)
print(user1.clean_email())




##########complete private variables we use __email by this the python will change the variable namemangling so it cant be accesed outside the class
#protected with _ and private __ 



