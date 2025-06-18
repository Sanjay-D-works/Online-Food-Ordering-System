from Models.User import User
from Models.UserManager import UserManager
from Controller.FoodManager import MainMenu

class LoginSystem:

    def Login(self):
        mailid = input("Email Id: ")
        password = input("Password: ")
        user = UserManager.FindUser(mailid, password)
        if user is not None:
            print("Login Successful...")
            menu = MainMenu()
            menu.Start()
        else:
            print("Invalid Email/Password. Please retry.")

    def Register(self):
        name = input("Name: ")
        mobile = int(input("Mobile No: "))
        mailid = input("Email Id: ")
        password = input("Password: ")
        user = User(name, mobile, mailid, password)
        UserManager.AddUser(user)
        print("Registration successful.")

    def GuestLogin(self):
        print("Welcome, Guest User!")
        menu = MainMenu()
        menu.Start()

    def Exit(self):
        print("Thank you for using our Food App...")
        exit(0)

    def ValidateOption(self, option):
        options = {
            1: self.Login,
            2: self.Register,
            3: self.GuestLogin,
            4: self.Exit
        }
        action = options.get(option)
        if action:
            action()
        else:
            print("Invalid Option")

class FoodApp:

    @staticmethod
    def Init():
        print("<< Welcome to Online Food Ordering System >>")
        loginSystem = LoginSystem()
        while True:
            print("\n--- Main Menu ---")
            print("1. Login\n2. Register\n3. Guest Login\n4. Exit")
            try:
                choice = int(input("Please Enter Your Choice: "))
                loginSystem.ValidateOption(choice)
            except ValueError:
                print("Invalid input. Please enter a number.")

