from Users.user import User
class Student(User):
    def __init__(self, name, email, Id, password, score:int):
        super().__init__(name, email, Id, password)
        self.score = score
   
    