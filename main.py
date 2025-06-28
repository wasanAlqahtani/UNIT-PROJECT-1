#Unit Project Wasan Alqahtani
import json
import re
from Users.teacher import Teacher 
import openai 
import os 
from dotenv import load_dotenv
load_dotenv()
openai.api_key= os.getenv("OPENAI_API_KEY")



users:list = []
'''
pip install openai
from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
'''
# 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
user_dictionary = {}
'''
def read_file(email:str, password:str):
    with open("user.json", "r", encoding = "UTF-8") as file:
        content = file.read()
        users = json.loads(content)
        for user in users:
            if user['email'] == email and user['password'] == password:
                return True
             
        return False
  '''     

def write_file(users:list):
      with open("user.json", "w" ,encoding= "UTF-8") as file:
            
            content = json.dumps(users, indent=2)
            file.write(content)

def check_email(email:str):
    valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
    if valid:
        return True
    else:
        print("Invalid Email Address")
        return False

def check_password(password:str):
    if len(password) >= 8:
        return True
    else:
        print("Invalid Password Try again")
        return False

def check_Id(Id:int):
    if len(Id) == 10:
        if Id in users:
            print("this Id ALready Exists")
            return False
        else:
            return True

def displayMenue_teacher():
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
                subject = input("Enter the subject (e.g. Math, Science): ")
                grade = input("Enter the grade level (e.g. 5th grade, high school): ")
                questions = generate_questions(subject, grade)

                print("\nGenerated Questions:\n" + "-"*40)
                for q in questions:
                    print(q + "\n")
            case "2":
                pass
            case "3":
                pass
            case "4":
                break
            case _:
                print("Wrong input try again!!!")
def generate_questions(subject: str, num_questions: int = 5) -> list:
    prompt = (
        f"Generate {num_questions} multiple-choice quiz questions for {subject} "
        f". Provide 4 options (A, B, C, D) and indicate the correct answer."
    )

    response =  client.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    content = response['choices'][0]['message']['content']
    return content.split("\n\n")
try:
        while True:
            
            print("Welcome to Quiz Gaming System")
            print("-"*20)
            print("[1]. Teacher")
            print("[2]. Student")
            print("[3]. Exit")
            print("-"*20)
            option = input("Please Enter what role you are: ")
            print("-"*20)

            if option == "1":
                print("Welcome to Login Page")
                print("[1]. Login")
                print("[2]. Register")
                login_choice = input("Please Enter What You Want: ")
                if login_choice == "1":
                    email = input("please enter your email: ")
                    password = input("please enter your password: ")
                    if check_email(email):
                        if read_file(email,password):
                           displayMenue_teacher()
                        else:
                            print("there no user in this email")
                        

                elif login_choice == "2":
                    print("Welcome to register Page")
                    name = input("please enter your name: ")
                    email = input ("please enter your email: ")
                    Id = int(input("please enter your id: "))
                    password = input("please enter your password: ")
                    subject = input("please enter your subject: ")
                    with open("user.json", "r", encoding="UTF-8") as file:
                        users = json.load(file)
                        email_exists = False
                    for user in users:
                        if user['email'].strip().lower() == email.strip().lower():
                            email_exists = True
                            break

                    if email_exists:
                        print("This email is already registered.")
                        continue

          
                    if(check_email(email) and check_password(password)):
                        teacher = Teacher(name, email, Id, password, subject)
                        user_dictionary = {
                        'name' : name, 
                        'email' : email,
                        'Id' : Id,
                        'password' : password, 
                        'subject' : subject,
                        }
                        users.append(user_dictionary)
                        
                        write_file(users)
                        displayMenue_teacher()
                    else:
                        print("wrong validation")
                   
                else:
                    print("Wrong input try again!!!")

            elif option == "2":
                print("Welcome")
                print("-"*20)
                print("[1]. Take a Quiz")
                print("[2]. Display Your Total Score")
                print("[3]. Show Statistics")
                print("[4]. Exit")
                choice = input("Please Enter What You Want: ")
                match choice:
                    case "1":
                        pass
                    case "2":
                        pass
                    case "3":
                        pass
                    case "4":
                        break
                    case _:
                        print("Wrong input try again!!!")
                
                break
            elif option == "3":
                break
            else:
                print("Wrong input try again!!!")
except Exception as e:
    print(e)

    






