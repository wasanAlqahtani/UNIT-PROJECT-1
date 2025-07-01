#Wasan ALqahtani
#subClass Teacher from user
#---------------------------------------------------------------------------------
'''This section for importing the librarys and pacakges'''
from Users.user import User
from  openai import OpenAI
import os 
import json
import random
import string 
from dotenv import load_dotenv
from colorama import init,Fore,Back,Style
init(autoreset=True)
load_dotenv()
client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))
#---------------------------------------------------------------------------------

class Teacher(User) :
    #Create initial method
    def __init__(self, name, email, Id, password, subject:str) -> None: 
        super().__init__(name, email,Id, password)
        self.__subject = subject

    #Create setter and getter od student score
    def set_subject(self, subject):
        self.__subject = subject

    def get_subject(self):
        return self.__subject
    
    #---------------------------------------------------------------------------------
    '''This section for methods that used by the teacher'''
    def generate_code(self, length):
        '''This method gave the teacher random code number for quiz and return the code'''
        letters = string.ascii_letters + string.digits
        session_code = ''.join(random.choices(letters, k=length))
        return session_code
    
    def generate_questions(self,code:str, subject:str, num_questions:int) -> list:
        '''This method take the code,subject,num of questions and the Open AI 
        generate questions and then add the questions to the dictionary
        and added to file it will return list with the questions'''
        #declare list and dectionary of questions
        generated_questions = []
        question_dictionary = {}

        #Make prompt for open ai to generate questions
        prompt = (
            f"Generate {num_questions} multiple-choice quiz questions for {subject} "
            f"Return the result in valid JSON format, with each question as an object with keys: "
            f"'question', 'options', and 'answer'.\n"
            f"'options' must be a dictionary with keys A, B, C, D.\n"
            f"Only return the JSON array."
           )
        #take the response from the open ai 
        response =  client.chat.completions.create(
            model="gpt-4", 
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        #strip the content by taking only the questions that is generated from the open ai
        content = response.choices[0].message.content.strip()
        #return json string into python object to read it 
        generated_questions = json.loads(content)

        #do loop to add lists in each question one for success student and one for failed students
        for each in generated_questions:
            each['failed_by'] = []
            each['success_by'] = []

        #add the code,subject,done by (email of the teacher) and the questions    
        question_dictionary = {
            'Quiz_code': code,
            'subject':subject,
            'done_by':self.get_email(),
            'question' : generated_questions,
        }
        #load the question file to take the question on list
        with open("question.json", "r" ,encoding= "UTF-8") as file:
             question_file = json.load(file)

        #append the dictionary to the list 
        question_file.append(question_dictionary)
        #dumps the json 
        with open("question.json", "w" ,encoding= "UTF-8") as file:
             content = json.dumps(question_file, indent=2)
             file.write(content)
        #return questions
        return generated_questions
    

    def students_details(self):
        '''This question will display the student detail (name and total score)'''
        try:
            #take the code from the teacher
            code = input("please enter the quiz code: ")
            #make list to take student that they do the quiz (set to avoid reputition)
            student_quiz = set()
            #open student and question files
            with open("student.json", "r", encoding="UTF-8") as file:
                students = json.load(file)
            with open("question.json", "r", encoding="UTF-8") as file:
                exams = json.load(file)
            flag = None
            #check if the code exits or not
            for quiz in exams:
                if code == quiz['Quiz_code'] and self.get_email() == quiz ['done_by']:
                    flag = quiz['question']
                    break
            if not flag: 
                print(Fore.RED + "there is no quiz with this code!")   
                return
            #add the student in the set
            for question in flag:
                student_quiz.update(question['success_by'])
                student_quiz.update(question['failed_by'])
            #if there is no students
            if not student_quiz:
                print(Fore.RED + "No student has take this quiz")
                return
            
            print("\n All Student Details:")
            print("-" * 20)
            #print the student detail one by one
            for student in students:
                if student['name'] in student_quiz:
                    print(f"Name: {student['name']}")
                    print(f"Score: {student['score']}")
                    print("-" * 20)
        except Exception as e:
           print(e)
    

    def display_statistics(self):
        '''This method will display statistics of the quiz each
        question who successed and who failed'''
        
        #take the code from the user 
        code = input("please enter the quiz code: ")
        #laod question file
        with open("question.json", "r", encoding="UTF-8") as file:
                exams = json.load(file)
        flag = None
        #check if the quiz exists or not
        for quiz in exams:
            if code == quiz['Quiz_code'] and self.get_email() == quiz ['done_by']:
                flag = quiz['question']
                break

        if not flag: 
            print(Fore.RED + "there is no quiz with this code!!")   
            return
        #print each question in detail and the student who success and who failed
        for i, question in enumerate(flag, 1):
            print(f"{i}. {question['question']} ")
            print(f"Answer. {question['answer']}")
            print(Fore.GREEN + f"\nThis question success by {len(question['success_by'])} students ->:")
            for student in question['success_by']:     
                print(f"{student} ")
            print(Fore.RED+ f"\nThis question failed by {len(question['failed_by'])} students ->: ")
            for student in question['failed_by']:     
                print(f"{student} ")
            
    def displayMenue_teacher(self):
        '''This method to display the menue for the Teacher and then take the input, based on it print the suitable operations'''
        try:
            while True:
                print("\nWelcome")
                print("-"*20)
                print("[1]. Generate Questions")
                print("[2]. Show All Studens In Details")
                print("[3]. Show Statistics")
                print("[4]. Exit")
                choice = input("Please Enter What You Want: ")
                match choice:
                    case "1":
                        while True: 
                            subject = input("Enter the subject: ")
                            if subject.isdigit() or len(subject)<2:
                                print(Fore.RED + "Wrong entry try again") 
                            else:
                                num_question = int(input("Enter number of questions: "))
                                if num_question == 0:
                                    print(Fore.RED + "Wrong entry try again") 
                                else: 
                                    code = self.generate_code(6)
                                    print(f"Quiz Code is: {code} ")
                                    questions = self.generate_questions(code,subject,num_question)
                                    print(Fore.YELLOW + "\nGenerated Questions:\n" + "-"*20)
                                    for q in questions:
                                        print(f"Q: {q['question']}")
                                        for option, Answers in q['options'].items():
                                            print(f"  {option}. {Answers}")
                                        print(f"Answer: {q['answer']}")
                                        print("-" * 20)
                                    break
                    case "2":
                        self.students_details()
                    case "3":
                        self.display_statistics()
                    case "4":
                        break
                    case _:
                        print(Fore.RED + "Wrong input try again!!!")
        except Exception as e :
            print(e)

    