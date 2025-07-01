#Unit Project Wasan Alqahtani

import json
import re
from Users.teacher import Teacher 
from Users.students import Student 
from colorama import init,Fore,Back,Style
init(autoreset=True)

teachers:list = []
teacher_dictionary = {}

students:list = []
student_dictionary = {}

#---------------------------------------------------------------------------------
'''
This part for methods (validations , read , write from files)
'''

def check_email(email:str)->bool:
        '''This Method take email as an arguments , and return boolean . 
        It's check the email validation using re package and give it 
        a pattern then if its right return true otherwise return false'''
        
        validation = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        if validation:
            return True
        else:
            print(Fore.RED + "Invalid Email Address")
            return False

def check_password(password:str)->bool:
        ''' This method take password and check the password length if its more than or equal to 8 return true
        otherwise return false'''

        if len(password) >= 8:
            return True
        else:
            print(Fore.RED + "Invalid Password")
            return False
            
def check_Id(Id:str)->bool:
        ''' This Method take Id and then check if the Id is 10 numbers and contain only numbers , it its true 
        return true otherwise return false'''

        if len(Id) == 10 and Id.isdigit():
           return True
        else:
            print(Fore.RED + "invalid id")
            return False

def read_file_teacher(email:str, password:str)-> list:
    '''This method take email and password and try to read from Teacher file to see if the user exists or not 
    then return list with this user'''

    with open("teacher.json", "r", encoding = "UTF-8") as file:
        content = file.read()
        teachers = json.loads(content)
        for teacher in teachers:
            if teacher['email'] == email and teacher['password'] == password:
                return teacher
              
def read_file_student(Id:str, password:str)-> list:
    '''This method take email and password and try to read from student file to see if the user exists or not 
    then return list with this user'''

    with open("student.json", "r", encoding = "UTF-8") as file:
        content = file.read()
        students = json.loads(content)
        for student in students:
            if student['email'] == email and student['password'] == password:
                return student
             
def write_file_teacher(teachers:list):
      '''This method take list and then write the contents of the list in teacher file'''

      with open("teacher.json", "w" ,encoding= "UTF-8") as file:
            content = json.dumps(teachers, indent=2)
            file.write(content)


def write_file_student(students:list):
      '''This method take list and then write the contents of the list in student file'''

      with open("student.json", "w" ,encoding= "UTF-8") as file:
            content = json.dumps(students, indent=2)
            file.write(content)

#---------------------------------------------------------------------------------
try:
        while True:
            #Print Welcome page
            print("-"*20)
            print("\nWelcome To Quiz System")
            print("-"*20)
            print("[1]. Teacher")
            print("[2]. Student")
            print("[3]. Exit")
            print("-"*20)
            #Take input from User
            option = input("Please Enter what role you are: ")
            print("-"*20)

#---------------------------------------------------------------------------------
           
            #Teacher Section
            #if the user enter 1 (Teacher) it will print Login Page 
            if option == "1":
                    while True:
                        print("\nWelcome to Login Page")
                        print("-"*20)
                        print("[1]. Login")
                        print("[2]. Register ")
                        print("[3]. Exit")
                        print("-"*20)

                        # Take input from User
                        login_choice = input("Please Enter What You Want: ")
                        print("-"*20)
                        #if the user enter 1 it will take email and password to log in 
                        if login_choice == "1":
                            email = input("please enter your email: ")
                            password = input("please enter your password (8 characters): ")
                            print("-"*20)
                            #check the validation of the email and password
                            if check_email(email) and check_password(password):
                                #read from the teacher file to see if the teacher exists or not 
                                teacher_list = read_file_teacher(email,password)
                                if not teacher_list:
                                    print(Fore.RED + "there is no user in this email")
                                else:
                                    print(Fore.GREEN + "The teacher was found")
                                    #if its exists create object and then call display menue in the teacher class to make operations
                                    teacher = Teacher(teacher_list['name'], teacher_list['email'],teacher_list['Id'],teacher_list['password'],teacher_list['subject'])
                                    #call display menue in teacher class
                                    teacher.displayMenue_teacher() 
                            

                        #if the user enter 2 it will take the required information to register this teacher and added it to the file            
                        elif login_choice == "2":
                            print("\nWelcome to register Page")
                            print("-"*20)
                            #take inputs from user
                            name = input("please enter your name: ")
                            email = input ("please enter your email: ")
                            Id = input("please enter your id: ")
                            password = input("please enter your password(8 characters): ")
                            subject = input("please enter your subject: ")
                            print("-"*20)
                            #create flag
                            exists = False
                            #the Id must be unique so the program will read from the teacher file to see if its exists or not
                            with open("teacher.json", "r", encoding="UTF-8") as file:
                                teachers = json.load(file)
                                for t in teachers :
                                    if t['Id'] == Id :
                                        print(Fore.RED + "This user is already registerd")
                                        exists = True
                                #check input validation before added it to the file
                                if check_email(email) and check_password(password) and check_Id(Id):
                                    if not exists:
                                        teacher = Teacher(name,email,Id,password,subject)
                                        print(Fore.GREEN + "Teacher Added Successfully")
                                        #create dictionary 
                                        teacher_dictionary = {
                                        'name' : name, 
                                        'email' : email,
                                        'Id' : Id,
                                        'password' : password, 
                                        'subject' : subject,
                                        }
                                        #add the dictionary to the list
                                        teachers.append(teacher_dictionary)
                                        #write the list to the file
                                        write_file_teacher(teachers)
                                        #call display menue in teacher class
                                        teacher.displayMenue_teacher()  

                        elif login_choice == "3":
                             break             
                        else:
                            print(Fore.RED + "Wrong input try again!!!")
                            
#---------------------------------------------------------------------------------

            #Student Section
            elif option == "2":
                while True: 
                    print("\nWelcome to Login Page")
                    print("-"*20)
                    print("[1]. Login")
                    print("[2]. Register")
                    print("[3]. Exit")
                    print("-"*20)

                    # Take input from User
                    login_choice = input("Please Enter What You Want: ")
                    print("-"*20)
                    #if the user enter 1 it will take email and password to log in
                    if login_choice == "1":
                        email = input("please enter your email: ")
                        password = input("please enter your password(8 characters) : ")
                        print("-"*20)

                        #if the user enter 1 it will take email and password to log in
                        if check_email(email) and check_password(password):
                             #read from the student file to see if the student exists or not 
                            student_list = read_file_student(email,password)
                            if not student_list:
                                print(Fore.RED + "there is no user in this email")

                            else:
                                #if its exists create object and then call display menue in the students class to make operations
                                print(Fore.GREEN + "The student was found")
                                student = Student(student_list['name'], student_list['email'],student_list['Id'],student_list['password'])
                                #call display menue in student class
                                student.displayMenue_students()
                     

                    #if the user enter 2 it will take the required information to register this student and added it to the file
                    elif login_choice == "2":

                        print("\nWelcome to register Page")
                        print("-"*20)
                        #take inputs from user
                        name = input("please enter your name: ")
                        email = input ("please enter your email: ")
                        Id = input("please enter your id: ")
                        password = input("please enter your password(8 characters) : ")
                        print("-"*20)
                        #create flag
                        email_exists = False
                        #the Id must be unique so the program will read from the student file to see if its exists or not
                        with open("student.json", "r", encoding="UTF-8") as file:
                            students = json.load(file)
                        for s in students:
                            if s['Id'].lower() == Id:
                                print(Fore.RED + "This user is already registerd")
                                email_exists = True
                         #check input validation before added it to the file
                        if check_email(email) and check_password(password) and check_Id(Id) :
                                if not email_exists:
                                    student = Student(name,email,Id,password)
                                    print(Fore.GREEN + "Students Added Successfully")
                                    #create dictionary
                                    student_dictionary = {
                                    'name' : name, 
                                    'email' : email,
                                    'Id' : Id,
                                    'password' : password, 
                                    'score': 0
                                    }
                                    #add the dictionary to the list
                                    students.append(student_dictionary)
                                    #write the list to the file
                                    write_file_student(students)
                                    #call display menue in studnet class
                                    student.displayMenue_students()  
                             
                    elif login_choice == "3":
                             break   
                    
                    else:
                        print(Fore.RED + "Wrong input try again!!!")



            elif option == "3":
                break
            else:
                print(Fore.RED + "Wrong input try again!!!")
except Exception as e:
    print(e.__class__)

    






