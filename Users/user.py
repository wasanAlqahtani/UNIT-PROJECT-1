import re

class User:

    def __init__(self, name:str, email:str, Id:str, password:str)->None:
        self.__name = name
        self.__email = email
        self.__Id = Id
        self.__password = password
    def set_name(self, name):
        self.__name = name
    
    def set_email(self, email):
        self.__email = email
    
    def set_Id(self, Id):
        self.__Id = Id
    
    def set_password(self, password):
        self.__password = password
    
    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def get_Id(self):
        return self.__Id
    
    def get_password(self):
        return self.__password
    
    
    def check_email(self, email:str)->bool:
        validation = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        if validation:
            self.set_email(email)
            return True
        else:
            print("Invalid Email Address")
            return False

    def check_password(self, password:str)->bool:
        if len(password) >= 8:
            self.set_password(password)
            return True

        else:
            print("Invalid Password Try again")
            return False

    def check_Id(self, Id:str)->bool:
        if len(Id) == 10:
           self.set_Id(Id)
           return True
        else:
            print("invalid id validation")
            return False
        







        
    