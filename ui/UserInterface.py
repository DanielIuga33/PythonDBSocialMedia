import uuid
from service.ServicePerson import ServicePerson
from utils.Prints import *
from utils.Functions import *


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
            password = input("Enter the person password: ")
            cnp = input("Enter the person cnp: ")
            birthday = input("Enter the person birthday(dd/mm/yyyy format): ")
            country = input("Enter the country of the person: ")
            province = input("Enter the province of the person: ")
            city = input("Enter the city: ")
            street = input("Enter the street: ")
            nr = input("Enter the number: ")
            self.__srv.add(idc, name, surname, email, password, cnp, birthday, country, province, city, street, nr)
        except ValueError as e:
            print(e)

    def ui_del_person(self):
        if self.__srv.size() == 0:
            print("No persons for now !")
            return
        for i in range(0, self.__srv.size()):
            print(f"[{i + 1}]-> {self.__srv.get_all()[i]}")
        print("-----------------------------------------------------")
        nb = int(input("Enter the number of the person you want to delete: "))
        if nb > self.__srv.size() or nb < 1:
            print("Invalid Person Number !")
            return
        self.__srv.delete(self.__srv.get_all()[nb-1].get_id_entity())

    def ui_update(self):
        if self.__srv.size() == 0:
            print("No persons for now !")
            return
        for i in range(0, self.__srv.size()):
            print(f"[{i + 1}]-> {self.__srv.get_all()[i]}")
        print("-----------------------------------------------------")
        nb = int(input("Enter the number of the person you want to update: "))
        if nb > self.__srv.size() or nb < 1:
            print("Invalid Person Number !")
            return
        yn = input("Do you want to change all the attributes?(Y/N): ")
        if yn not in ["Y", "y", "N", "n"]:
            print("Invalid choice !")
            return
        elif yn in ["Y", "y"]:
            name = input("Enter the person name: ")
            surname = input("Enter the person surname: ")
            email = input("Enter the person email: ")
            password = input("Enter the person password: ")
            cnp = input("Enter the person cnp: ")
            birthday = input("Enter the person birthday(dd/mm/yyyy format): ")
            country = input("Enter the country of the person: ")
            province = input("Enter the province of the person: ")
            city = input("Enter the city: ")
            street = input("Enter the street: ")
            nr = input("Enter the number: ")
            self.__srv.update(name, surname, email, password, cnp, birthday, country, province, city, street, nr,
                              self.__srv.get_all()[nb-1].get_id_entity())
        elif yn in ["N", "n"]:
            print("[1] name       [7] country ")
            print("[2] surname    [8] province")
            print("[3] email      [9] city")
            print("[4] password   [10] street")
            print("[5] cnp        [11] nr")
            print("[6] birthday   [x] Exit")
            string = input("Enter the attributes you want \n to change separated by commas:")
            lista = string.split(",")
            u_list = list(set(lista))
            if "x" in lista:
                return
            else:
                person = self.__srv.get_all()[nb-1]
                name = ""
                surname = ""
                email = ""
                password = ""
                cnp = ""
                birthday = ""
                country = ""
                province = ""
                city = ""
                street = ""
                nr = ""
                for elem in u_list:
                    match elem:
                        case "1":
                            name = input("Enter the person name: ")
                        case "2":
                            surname = input("Enter the person surname: ")
                        case "3":
                            email = input("Enter the person")
                        case "4":
                            password = input("Enter the person password: ")
                        case "5":
                            cnp = input("Enter the person cnp: ")
                        case "6":
                            birthday = input("Enter the person birthday(dd/mm/yyyy format): ")
                        case "7":
                            country = input("Enter the country of the person: ")
                        case "8":
                            province = input("Enter the province of the person: ")
                        case "9":
                            city = input("Enter the city: ")
                        case "10":
                            street = input("Enter the street: ")
                        case "11":
                            nr = input("Enter the number: ")
                if name == "":
                    name = person.get_name()
                if surname == "":
                    surname = person.get_surname()
                if email == "":
                    email = person.get_email()
                if password == "":
                    password = person.get_password()
                if cnp == "":
                    cnp = person.get_cnp()
                if birthday == "":
                    birthday = person.get_birthday()
                if country == "":
                    country = person.get_country()
                if province == "":
                    province = person.get_province()
                if city == "":
                    city = person.get_city()
                if street == "":
                    street = person.get_street()
                if nr == "":
                    nr = person.get_nr()
                self.__srv.update(name, surname, email, password, cnp, birthday, country, province, city, street, nr,
                                  person.get_id_entity())

    def ui_show_all(self):
        for elem in self.__srv.get_all():
            print(elem)
