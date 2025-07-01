#Wasan Alqahtani
#subClass Student from user
#---------------------------------------------------------------------------------
'''This section for importing the librarys and pacakges'''
from Users.user import User
import json
from  openai import OpenAI
from colorama import init,Fore,Back,Style
import os
from dotenv import load_dotenv
load_dotenv()
init(autoreset=True)
#Generate OpenAI
client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))
#---------------------------------------------------------------------------------

class Student(User):
    #Create initial method
    def __init__(self, name, email, Id, password, score:int = 0) -> None:
        super().__init__(name, email, Id, password)
        self.__score = score

    #Create setter and getter od student score
    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score
    #---------------------------------------------------------------------------------

    '''This section for methods that used by the student'''

    def improve_answers(self,failed_questions):

        '''This method takes list that containd the failed question that the user did and then call the OpenAi
        to generate some tips to help the user to improve 
        '''

        print(Fore.YELLOW + "Generate some tips to improve based on your weaknesses...\n")
        #Prompt the openAi to generate tips that is easy and helpful to improve 
        prompt = (
                "The following are questions a student answered incorrectly in a quiz.\n"
                "For each one, provide a simple and clear explanation and a helpful tip to improve.\n"
                "Do not print the question and the answer in the explanation"
                "Use easy language suitable for beginners.\n\n"
            )
        #Added the failed question to the prompt
        for question in failed_questions:
            prompt += f"- {question}\n"

        #take the response from Open Ai 
        response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
        #take the respons and strip it to make it in lines 
        explanation = response.choices[0].message.content.strip()
        print("Tips to Improve: ")
        print("-" * 20)
        print(explanation)
        print("-" * 20)


    def display_qestion(self):

        '''This method it will display the questions to the student based on the quize code 
        and check if the student already take the exam or not '''
        
        #get the score of the student from get score that is declared in user classs
        score = self.get_score()
        # declare failed list to add the questions that the user failed it to use it in the improvment
        failed = []
        #read the student file to take the student 
        with open("student.json","r",encoding="UTF-8") as f:
            students = json.load(f)
        #take the quiz code from the student
        code = input("Please Enter the quiz code: ")
        #read the question file to display the questions based on the quize code
        with open("question.json", "r", encoding="UTF-8") as file:
                exams = json.load(file)
        # add flags one to check if the code is in the file or not and the other is to add the questions
        flag = None
        quiz_exists = False
        for quiz in exams:
            if code == quiz['Quiz_code']:
                quiz_exists = True
                for question in quiz['question']:
                   if (self.get_name() in question['failed_by']) or (self.get_name() in question['success_by']):
                      flag = True
                      break
                if not flag :     
                   flag = quiz['question']
                else : 
                    print(Fore.RED + "You Already Take the Quiz")
                    return
        if not quiz_exists: 
            print(Fore.RED + "there is no quiz with this code!")   
            return 
        #create loop to print the questions one by one and let the user enter the answer and then print the other question
        for i, q in enumerate(flag, 1):
            print(f"\nQ{i}: {q['question']}")
            for key, value in q['options'].items():
                print(f"  {key}. {value}")
            #take the Answer from the student
            answer = input("Your answer (please write the letter only): ").strip().upper()
            #check if the answer is correct or not 
            if answer == q['answer']:
                print(Fore.GREEN + "Correct!" + Style.RESET_ALL)
                # increment the score of this student
                score += 1   
                self.set_score(score)
                #add the student name in success by section of the question in the dictionary and the json
                q['success_by'].append(self.get_name())    
            else:
                 #add the student name in failed by section of the question in the dictionary and the json
                print(Fore.RED + "Incorrect" + Style.RESET_ALL)
                q['failed_by'].append(self.get_name())
                failed.append(q["question"])
                #update the student score by search of the student based on its id and then update it 
        for student in students :
            if str(student['Id']) == str(self.get_Id()):
                student['score'] = score
                break
         #write all changes in the files   
        with open("student.json","w",encoding="UTF-8") as f:
             json.dump(students,f, indent=2)
        with open("question.json", "w", encoding="UTF-8") as file:
            json.dump(exams, file, indent=2)

        try:
            #if the student fail in some qestion it will call improve answers method to take some tips from open ai
            if failed:
                self.improve_answers(failed)
            else:
                print(Fore.GREEN + "You answered all questions Right.")
        except Exception as e:
            print(e)

    def displayMenue_students(self):
        '''This method to display the menue for the sttudent and then take the input, based on it print the suitable operations'''
        try :
            while True:
                print("\nWelcome")
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
                        print(Fore.RED + "Wrong input try again!!!")
        except Exception as e:
            print(e)