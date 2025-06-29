from Users.user import User
import json
class Student(User):
    def __init__(self, name, email, Id, password, score:int = 0) -> None:
        super().__init__(name, email, Id, password)
        self.__score = score

   
    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score
    
    def display_qestion(self):
        with open("question.json", "r", encoding="UTF-8") as file:
                questions = json.load(file)

        score = 0
        for i, q in enumerate(questions, 1):
            print(f"\nQ{i}: {q['question']}")
            for key, value in q["options"].items():
                print(f"  {key}. {value}")

            answer = input("Your answer (A/B/C/D): ").strip().upper()
            if answer == q["answer"]:
                print("✅ Correct!")
                self.set_score(self.get_score()+1) 
            else:
                print(f" Incorrect. Correct answer is: {q['answer']}")

    def displayMenue_students(self):
        while True:
            print("Welcome")
            print("-"*20)
            print("[1]. Take a quiz")
            print("[2]. Help me to improve")
            print("[3]. Show Statistics")
            print("[4]. Show total score")
            print("[5]. Exit")
            choice = input("Please Enter What You Want: ")
            match choice:
                case "1":
                    self.display_qestion()
                    
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    break
                case _:
                    print("Wrong input try again!!!")