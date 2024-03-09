import uuid

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
        try:
            email = email_login(self.__srv_pr)
            password = password_login(self.__srv_pr)
            print("\tHi " + self.__srv_pr.find_login(email, password).get_surname() + " :) !\n")
            print("Logging in...")
            return self.__srv_pr.find_login(email, password)
        except ValueError:
            return None

    def user_register(self):
        try:
            name = string_input("name")
            surname = string_input("surname")
            email = email_register(self.__srv_pr)
            password = password_register()
            print("Registration was completed successfully !")
            print("\tHi " + surname + " do you want to add some personal \n about you? ")
            print("\t [1] Yes \n\t [2] Later")
            option = input("\nEnter your choice: ")
            if option == "1":
                try:
                    cnp = string_input("cnp")
                except ValueError:
                    cnp = ""
                birthday = input("Enter the person birthday(dd/mm/yyyy format): ")
                country = input("*Enter the country of the person: ")
                province = input("*Enter the province of the person: ")
                city = input("*Enter the city/village of the person: ")
                street = input("*Enter the street: ")
                nr = input("*Enter the number: ")
                self.__srv_pr.add(uuid.uuid4(), name, surname, email, password, cnp, birthday, country,
                                  province, city, street, nr)
            else:
                self.__srv_pr.add(uuid.uuid4(), name, surname, email, password, "", "", "",
                                  "", "", "", "")

        except ValueError:
            return None

    def user_handler(self, person):
        pass
