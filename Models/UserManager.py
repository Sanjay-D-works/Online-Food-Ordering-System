from Models.User import User

class UserManager:
    __User = []

    @classmethod
    def AddUser(cls, user):
        if isinstance(user, User):
            cls.__User.append(user)
            print("You have been successfully registered")
        else:
            print("Invalid User")

    @classmethod
    def FindUser(cls, mailid, pwd):
        for user in cls.__User:
            if user.MailId == mailid and user.Password == pwd:
                return user
        return None