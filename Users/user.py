class User:

    def __init__(self, name:str, email:str, Id:int, password:str)->None:
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
    
    



        
    