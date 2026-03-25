"""
sign-up subroutine for demo purposes
serves as exammple for project task 
"""

#usernames to be saved after signing up
DB_USERNAME_1 = ""
DB_USERNAME_2 = ""
#passwords to be saved after signing up
DB_PASSWORD_1 = ""
DB_PASSWORD_2 = ""
#greeting
print("Hello!")
print("Would you like to Sign up or Login?")
#ask to sign-up or login until option is chosen
registred = ""
while registred == "":
    print("To SIGN-UP enter 1")
    print("To LOGIN enter 2")
    register_or_login = input()

    #select subroutine - sign up or login
    if register_or_login == "1":
        registred = False
    elif register_or_login == "2":
        registred = True
    else:
        print("Wrong input")
#sign-up subroutine
if not registred:
    #ask for usernames
    DB_USERNAME_1 = input("Eneter usrname for player 1")
    DB_USERNAME_2 = input("Eneter usrname for player 2")
    #ask for passwords
    DB_PASSWORD_1 = input("Eneter password for player 1")
    DB_PASSWORD_2 = input("Eneter password for player 2")
    registred = True
    print("Usernames and passwords for the two users are set")
login = False   
while not login:
    print("Would you like to login or quite?")
    want_lognin = input(" - type y for yes or n for no or q for quite\n")
    if want_lognin.lower() == "y":
        login = True
    elif want_lognin.lower() == "n":
        login = False
    elif want_lognin.lower() == "q":
        print("Quitting")
        break
    else:
        print("Wrong input")
#login subroutine
if registred and login:
    print("LOGIN PAGE")
    print("This part of code is for students to develop independently!")
