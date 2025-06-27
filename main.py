#Unit Project Wasan Alqahtani
import json

from Users.teacher import Teacher 
from Users.user import User
users:list = []
user_dictionary = {}
def read_file(email:str, password:str):
    with open("user.json", "r", encoding = "UTF-8") as file:
        content = file.read()
        users = json.loads(content)
        for user in users:
            if user["email"] == email and user["password"]==password:
                return True
            else:
                return False

def write_file(users):
      with open("user.json", "w" ,encoding= "UTF-8") as file:
            
            content = json.dumps(users)
            file.write(content)

    


try:
    with open("user.json", "r", encoding = "UTF-8") as file:
        content = file.read()
        users = json.loads(content)
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

                    if read_file(email,password):
                        print("welcome")
                    else:
                        print("wrong entry ")

                elif login_choice == "2":
                    print("Welcome to register Page")
                    name = input("please enter your name: ")
                    email = input ("please enter your email: ")
                    Id = input("please enter your id: ")
                    password = input("please enter your password: ")
                    subject = input("please enter your subject: ")
                    
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
                   
                else:
                    print("Wrong input try again!!!")
                
                print("Welcome")
                print("-"*20)
                print("[1]. Generate Questions")
                print("[2]. Show All Studens In Details")
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

    






