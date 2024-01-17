from datetime import datetime
import uuid
from getpass import getpass

from service.ServicePerson import ServicePerson
from utils.Prints import *


class UserInterface:
    def __init__(self, srv: ServicePerson):
        self.__srv = srv

    def run(self):
        while True:
            print_person_menu()
            choice = input("Give here your choice: ")
            match choice:
                case "1":
                    self.ui_add_person()
                case "2":
                    self.ui_del_person()
                case "3":
                    self.ui_update()
                case "a":
                    self.ui_show_all()
                case "x":
                    break
                case _:
                    print("Invalid choice !")

    def ui_add_person(self):
        try:
            idc = uuid.uuid4()
            name = input("Enter the person name: ")
            surname = input("Enter the person surname: ")
            email = input("Enter the person email: ")
            password = getpass("Enter the person password: ")
            cnp = input("Enter the person cnp: ")
            array = input("Enter the person birthday(dd/mm/yyyy format): ")
            array = array.split("/")
            birthday = datetime(int(array[0]), int(array[1]), int(array[2]))
            country = input("Enter the country of the person: ")
            province = input("Enter the province of the person: ")
            city = input("Enter the city: ")
            street = input("Enter the street: ")
            nr = input("Enter the number: ")
            self.__srv.add(idc, name, surname, email, password, cnp, birthday, country, province, city, street, nr)
        except ValueError as e:
            print(e)

    def ui_del_person(self):
        pass

    def ui_update(self):
        pass

    def ui_show_all(self):
        pass
