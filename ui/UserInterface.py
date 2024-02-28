import uuid

from domain.Friendship import Friendship
from service.ServicePerson import ServicePerson
from ui.Admin import Admin
from utils.Prints import *
from utils.Functions import *


class UserInterface:
    def __init__(self, srv_pr, srv_fr):
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
        return None

    def user_register(self):
        return None

    def user_handler(self, person):
        pass
