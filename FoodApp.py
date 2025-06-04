<<<<<<< HEAD
from FoodApp import FoodApp

    def Init():
        print("Welcome from GitHub version")
        print("This part is added from local version")


FoodApp.Init()
=======
#Online Food Ordering System

from Models.User import User
from Models.UserManager import UserManager

class LoginSystem:
    
    def Login(self):
        
        mailid = input("Email Id: ")
        password = input("Password: ")

        user = UserManager.FindUser(mailid, password)

        if user is not None:
            pass #Next Step
        else:
            print("Invalid Mail/password.... Please Retry")

    def Register(self):
        
        name = input("Name: ")
        mobile = int(input("mobile No: "))
        mailid = input("Email Id: ")
        password = input("Password: ")

        user = User(name,mobile,mailid,password)

        UserManager.AddUser(user)
        

    def GuestLogin(self):
        pass

    def ValidateOption(self, option):
        
        if option == 1:
            self.Login()
        elif option == 2:
            self.Register()
        elif option == 3:
            self.GuestLogin(self)
        elif option == 4:
            print("Thank you for using our Food App...")
            exit()
        else:
            print("Invalid Choice.. please Retry")
 
class FoodApp:
    
    LoginOption = {1:"Login",2:"Register",3:"Guest",4:"Exit"}

    @staticmethod
    def Init(): # Initial Method
        print("<<Welcome to Online Food Ordering>>")

    loginSystem = LoginSystem()

    while True:
        for option in FoodApp.LoginOption:
            print(f"{option}.{FoodApp.LoginOption[option]}", end = " ")
        print()


        try:
            choice = int(input("Please Enter Your Choice : "))
            loginSystem.ValidateOption(choice)
        except ValueError:
            print("Invalid input.. Please Enter the Valid choice")

>>>>>>> 4c28a89 (Adding the Models for FoodApp.py)
