#Unit Project Wasan Alqahtani
import json
import re
from Users.teacher import Teacher 
from Users.students import Student 
teachers:list = []
teacher_dictionary = {}

students:list = []
student_dictionary = {}

#####################################################################################################

def read_file_teacher(email:str, password:str):
    with open("teacher.json", "r", encoding = "UTF-8") as file:
        content = file.read()
        teachers = json.loads(content)
        for teacher in teachers:
            if teacher['email'] == email and teacher['password'] == password:
                return True
             
        return False
    
def read_file_student(email:str, password:str):
    with open("student.json", "r", encoding = "UTF-8") as file:
        content = file.read()
        students = json.loads(content)
        for student in students:
            if student['email'] == email and student['password'] == password:
                return True
             
        return False


def write_file_teacher(teachers:list):
      with open("teacher.json", "w" ,encoding= "UTF-8") as file:
            content = json.dumps(teachers, indent=2)
            file.write(content)


def write_file_student(teachers:list):
      with open("student.json", "w" ,encoding= "UTF-8") as file:
            content = json.dumps(students, indent=2)
            file.write(content)

#####################################################################################################
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
               # teacher = Teacher(name, email, Id,password,subject)
                print("Welcome to Login Page")
                print("[1]. Login")
                print("[2]. Register ")
                login_choice = input("Please Enter What You Want: ")
                if login_choice == "1":
                    email = input("please enter your email: ")
                    password = input("please enter your password: ")
                    name:str = ""
                    subject:str = ""
                    Id = ""
                    with open("teacher.json", "r", encoding = "UTF-8") as file:
                        for teacher in teachers:
                            if teacher['email'] == email :
                                name = teacher['name']
                                subject = teacher['subject']
                    
                    teacher = Teacher(name, email, Id,password,subject)
                    if teacher.check_email(email) and teacher.check_password(password):
                        if read_file_teacher(email,password):
                           teacher.displayMenue_teacher()
                        else:
                           print("there is no user in this email")
                        

                elif login_choice == "2":

                    print("Welcome to register Page")
                    name = input("please enter your name: ")
                    email = input ("please enter your email: ")
                    Id = input("please enter your id: ")
                    password = input("please enter your password: ")
                    subject = input("please enter your subject: ")
                    teacher = Teacher(name,email,Id,password,subject)
                    teacher.set_name(name)
                    teacher.set_subject(subject)
                    exists = False
                    with open("teacher.json", "r", encoding="UTF-8") as file:
                        teachers = json.load(file)
                        for t in teachers :
                            if t['Id'] == Id :
                                print("This user is already registerd")
                                exists = True
                    
                        if teacher.check_email(email) and teacher.check_password(password) and teacher.check_Id(Id) :
                            if not exists:
                                teacher_dictionary = {
                                'name' : name, 
                                'email' : email,
                                'Id' : Id,
                                'password' : password, 
                                'subject' : subject,
                                }
                                teachers.append(teacher_dictionary)
                                write_file_teacher(teachers)
                                teacher.displayMenue_teacher()
                        
                   
                else:
                    print("Wrong input try again!!!")
                    

#####################################################################################################

            elif option == "2":
                print("Welcome to Login Page")
                print("[1]. Login")
                print("[2]. Register")
                login_choice = input("Please Enter What You Want: ")
                if login_choice == "1":
                    name:str = ""
                    subject:str = ""
                    Id = ""
                    email = input("please enter your email: ")
                    password = input("please enter your password: ")
                    student = Student(name, email, Id,password)
                    if student.check_email(email) and student.check_password(password):
                        if read_file_student(email,password):
                           student.displayMenue_students()
                        else:
                           print("there is no user in this email")
                           
                elif login_choice == "2":
                    print("Welcome to register Page")
                    name = input("please enter your name: ")
                    email = input ("please enter your email: ")
                    Id = input("please enter your id: ")
                    password = input("please enter your password: ")  
                    student = Student(name,email,Id,password)
                    student.set_name(name)
                    with open("student.json", "r", encoding="UTF-8") as file:
                        students = json.load(file)
                        email_exists = False
                    for s in students:
                        if s['email'].lower() == email.lower():
                            print("This user is already registerd")
                            email_exists = True

                    if student.check_email(email) and student.check_password(password) and student.check_Id(Id) :
                            if not email_exists:
                                student_dictionary = {
                                'name' : name, 
                                'email' : email,
                                'Id' : Id,
                                'password' : password, 
                                'score': 0
                                }
                                students.append(student_dictionary)
                                write_file_student(students)
                                student.displayMenue_students()        
                   
                else:
                    print("Wrong input try again!!!")
                    
            elif option == "3":
                break
            else:
                print("Wrong input try again!!!")
except Exception as e:
    print(e)

    






