from Users.user import User
import json
from  openai import OpenAI
from colorama import Fore,Back,Style
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))
class Student(User):
    def __init__(self, name, email, Id, password, score:int = 0) -> None:
        super().__init__(name, email, Id, password)
        self.__score = score

   
    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score
    
    def improve_answers(self,failed_questions):

        '''method to improve student in the concept that he answer wrong on it
        '''
        print("Generate tips for you to improve based on your answers...\n")
        prompt = (
                "The following are questions a student answered incorrectly in a quiz.\n"
                "For each one, provide a simple and clear explanation and a helpful tip to improve.\n"
                "Use easy language suitable for beginners.\n\n"
            )
        for q in failed_questions:
            prompt += f"- {q}\n"

            # Ask OpenAI to give help (you can replace client with your actual OpenAI setup)
        response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
        explanation = response.choices[0].message.content.strip()
        print("Tips to Improve: ")
        print("-" * 40)
        print(explanation)
        print("-" * 40)


    def display_qestion(self):
        score = self.get_score()
        failed = []
        with open("student.json","r",encoding="UTF-8") as f:
            students = json.load(f)
        code = input("Please Enter the quiz code: ")
        with open("question.json", "r", encoding="UTF-8") as file:
                exams = json.load(file)
       # flag = None
        flag = None
        for quiz in exams:
            if code == quiz['Quiz_code']:
                flag = quiz['question']
               # flag = quiz
                break
        if not flag: 
            print("there is no quiz with this code!!")   
            return
        
        for i, q in enumerate(flag, 1):
            print(f"\nQ{i}: {q['question']}")
            for key, value in q["options"].items():
                print(f"  {key}. {value}")

            answer = input("Your answer (A/B/C/D): ").strip().upper()
            if answer == q['answer']:
                print(Fore.GREEN + "Correct!" + Style.RESET_ALL)
                score += 1   
                self.set_score(score)
                q['success_by'].append(self.get_name())    
            else:
                print(Fore.RED + "Incorrect" + Style.RESET_ALL)
                q['failed_by'].append(self.get_name())
                failed.append(q["question"])
        for student in students :
            if str(student['Id']) == str(self.get_Id()):
                student['score'] = score
                break
            
        with open("student.json","w",encoding="UTF-8") as f:
             json.dump(students,f, indent=2)
        with open("question.json", "w", encoding="UTF-8") as file:
            json.dump(exams, file, indent=2)
        if failed:
            self.improve_answers(failed)
        else:
            print("You answered all questions Right.")

    def help_toimprove(self):
        pass

    def displayMenue_students(self):
        while True:
            print("Welcome")
            print("-"*20)
            print("[1]. Take a quiz")
            print("[2]. Show total score")
            print("[3]. Exit")
            choice = input("Please Enter What You Want: ")
            match choice:
                case "1":
                    self.display_qestion()
                case "2":
                     print(f"Your Total Score is: {self.get_score()}")
                case "3":
                    break
                case _:
                    print("Wrong input try again!!!")