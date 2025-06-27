from user import User

class Teacher(User) :
    def __init__(self, name, email, Id, password, subject:str):
        super().__init__(name, email,Id, password)
        self.subject = subject