#Super Class
class User:
    #Create Initial method 
    def __init__(self, name:str, email:str, Id:str, password:str)->None:
        self.__name = name
        self.__email = email
        self.__Id = Id
        self.__password = password

    # Create Setters and Getters
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
    
        







        
    