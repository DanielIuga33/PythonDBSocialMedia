import uuid

from domain.Friendship import Friendship
from domain.Personvalidator import PersonValidator
from service.ServicePerson import ServicePerson
from ui.Admin import Admin
from utils.Prints import *
from utils.Functions import *


class UserInterface:
    def __init__(self, srv_pr: ServicePerson, srv_fr):
        self.__srv_pr = srv_pr
        self.__srv_fr = srv_fr
        self.__admin = Admin(self.__srv_pr, self.__srv_fr)

    def run(self):
        while True:
            print_main_menu()
            choice = input("Give here your choice: ")
            match choice:
                case "1":
                    user_login = self.user_login()
                    if self.user_login is not None:
                        self.user_handler(user_login)
                case "2":
                    if self.user_register() is not None:
                        user_login = self.user_login()
                        if self.user_login is not None:
                            self.user_handler(user_login)
                case "admin":
                    self.__admin.run()
                case "x":
                    break
                case _:
                    print("Invalid choice !")

    def user_login(self):
        email = input(" email: ")
        password = input(" password: ")
        while self.__srv_pr.find_login(email, password) is None:
            print("Invalid email or password !\nPlease try again or type x to quit.")
            email = input(" email: ")
            if email == "x" or email == "X":
                return None
            password = input(" password: ")
            if password == "x" or password == "X":
                return None
        return self.__srv_pr.find_login(email, password)

    def user_register(self):
        validator = PersonValidator()
        email = email_input(self.__srv_pr, validator)
        password = input(" password: ")

    def user_handler(self, person):
        pass
