from Users.user import User
from  openai import OpenAI
import os 
import json
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
    
    def generate_questions(self,subject:str, num_questions:int) -> list:
        generated_questions = []
        question_dictionary = {}
        prompt = (
            f"Generate {num_questions} multiple-choice quiz questions for {subject} "
            f". Provide 4 options (A, B, C, D) and indicate the correct answer."
        )

        response =  client.chat.completions.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        content = response.choices[0].message.content
        questions = content.strip().split("\n\n")
        for question in questions:
            question_line = question.strip().split("\n")
            if len(question_line) < 6:
                 continue 
            thequestion = question_line[0].strip()
            options = {
                "A": question_line[1].strip()[2:].strip(),
                "B": question_line[2].strip()[2:].strip(),
                "C": question_line[3].strip()[2:].strip(),
                "D": question_line[4].strip()[2:].strip(),
            }
            answer = question_line[5].strip().split("Answer:")[-1].strip()
            question_dictionary = {
                'question' : thequestion,
                'options': options,
                'answer' : answer
            }
            generated_questions.append(question_dictionary)
        with open("question.json", "w" ,encoding= "UTF-8") as file:
             content = json.dumps(generated_questions, indent=2)
             file.write(content)

        return generated_questions
    

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
                    questions = self.generate_questions(subject,num_question)

                    print("\nGenerated Questions:\n" + "-"*40)
                    for q in questions:
                        print(f"Q: {q['question']}")
                        for option, text in q['options'].items():
                            print(f"  {option}. {text}")
                        print(f"Answer: {q['answer']}")
                        print("-" * 40)
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    break
                case _:
                    print("Wrong input try again!!!")


    