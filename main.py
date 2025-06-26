#Unit Project Wasan Alqahtani
from Users import *
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
           pass
        elif login_choice == "2":
           pass
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


    






