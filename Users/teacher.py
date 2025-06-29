from Users.user import User

class Teacher(User) :
    def __init__(self, name, email, Id, password, subject:str):
        super().__init__(name, email,Id, password)
        self.__subject = subject


    