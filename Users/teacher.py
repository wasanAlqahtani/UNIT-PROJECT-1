from Users.user import User
from  openai import OpenAI
import os 
import json
import secrets
import string 
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))

class Teacher(User) :
    def __init__(self, name, email, Id, password, subject:str) -> None: 
        super().__init__(name, email,Id, password)
        self.__subject = subject


    def set_subject(self, subject):
        self.__subject = subject

    def get_subject(self):
        return self.__subject
    
    def generate_code(self, length=32):
        letters = string.ascii_letters + string.digits
        session_code = ''.join(secrets.choice(letters) for i in range(length))
        return session_code
    
    def generate_questions(self,code:str, subject:str, num_questions:int) -> list:
        generated_questions = []
        question_dictionary = {}
        prompt = (
            f"Generate {num_questions} multiple-choice quiz questions for {subject} "
            f"Return the result in valid JSON format, with each question as an object with keys: "
            f"'question', 'options', and 'answer'.\n"
            f"'options' must be a dictionary with keys A, B, C, D.\n"
            f"Only return the JSON array."
           )

        response =  client.chat.completions.create(
            model="gpt-4", 
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        content = response.choices[0].message.content.strip()
        generated_questions = json.loads(content)
        for each in generated_questions:
            each['failed_by'] = []
            each['success_by'] = []
            
        question_dictionary = {
            'Quiz_code': code,
            'subject':subject,
            'done_by':self.get_email(),
            'question' : generated_questions,
        }
        with open("question.json", "r" ,encoding= "UTF-8") as file:
             question_file = json.load(file)


        question_file.append(question_dictionary)
        with open("question.json", "w" ,encoding= "UTF-8") as file:
             content = json.dumps(question_file, indent=2)
             file.write(content)

        return generated_questions
    
    def students_details(self):
        try:
            with open("student.json", "r", encoding="UTF-8") as file:
                students = json.load(file)

            print("\n📋 All Student Details:")
            print("-" * 40)
            for student in students:
                print(f"Name: {student['name']}")
                print(f"Score: {student['score']}")
                print("-" * 40)
        except Exception as e:
           print("e")
    
    def display_statistics(self):
        code = input("please enter the quiz code: ")
        with open("question.json", "r", encoding="UTF-8") as file:
                exams = json.load(file)
        flag = None
        for quiz in exams:
            if code == quiz['Quiz_code']:
                flag = quiz['question']
               # flag = quiz
                break
        if not flag: 
            print("there is no quiz with this code!!")   
            return
        for i, question in enumerate(flag, 1):
            print(f"{i}. {question['question']} ")
            print(f"Answer. {question['answer']}")
            print(f"This question success by {len(question['success_by'])} students ->: {question['success_by']}")
            print(f"This question failed by {len(question['failed_by'])} students ->: {question['failed_by']}")

    
    def displayMenue_teacher(self):
        while True:
            print("Welcome")
            print("-"*20)
            print("[1]. Generate Questions")
            print("[2]. Show All Studens In Details")
            print("[3]. Show Statistics")
            print("[4]. Exit")
            choice = input("Please Enter What You Want: ")
            match choice:
                case "1":
                    subject = input("Enter the subject: ")
                    num_question = int(input("Enter number of questions: "))
                    code = self.generate_code(6)
                    print(f"Quiz Code is: {code} ")
                    questions = self.generate_questions(code,subject,num_question)
                    print("\nGenerated Questions:\n" + "-"*40)
                    for q in questions:
                        print(f"Q: {q['question']}")
                        for option, text in q['options'].items():
                            print(f"  {option}. {text}")
                        print(f"Answer: {q['answer']}")
                        print("-" * 40)
                case "2":
                    self.students_details()
                case "3":
                    self.display_statistics()
                case "4":
                    break
                case _:
                    print("Wrong input try again!!!")


    