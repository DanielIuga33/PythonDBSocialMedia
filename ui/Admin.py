import uuid

from domain.Friendship import Friendship
from utils.Prints import *
from utils.Functions import *


class Admin:
    def __init__(self, srv_pr, srv_fr):
        self.__srv_pr = srv_pr
        self.__srv_fr = srv_fr

    def run(self):
        while True:
            print_admin_main_menu()
            choice = input("Give here your choice: ")
            match choice:
                case "1":
                    self.person_menu()
                case "2":
                    self.friendship_menu()
                case "x":
                    break
                case _:
                    print("Invalid choice !")

    def person_menu(self):
        while True:
            print_admin_person_menu()
            choice = input("Give here your choice: ")
            match choice:
                case "1":
                    self.ui_add_person()
                case "2":
                    self.ui_del_person()
                case "3":
                    self.ui_update_person()
                case "a":
                    self.ui_show_all_ps()
                case "x":
                    break
                case _:
                    print("Invalid choice !")

    def friendship_menu(self):
        if self.__srv_pr.size() <= 1:
            print("You have to add at least 2 persons !")
            return
        while True:
            print_admin_friendship_menu()
            choice = input("Give here your choice: ")
            match choice:
                case "1":
                    self.ui_add_friendship()
                case "2":
                    self.ui_del_friendship()
                case "3":
                    self.ui_update_friendship()
                case "a":
                    self.ui_show_all_fr()
                case "x":
                    break
                case _:
                    print("Invalid choice !")

        # --{ PERSON MENU }----------------------------------------------------------------------------------------

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
            city = input("Enter the city/village of the person: ")
            street = input("Enter the street: ")
            nr = input("Enter the number: ")
            self.__srv_pr.add(idc, name, surname, email, password, cnp, birthday, country, province, city, street, nr)
        except ValueError as e:
            print(e)

    def ui_del_person(self):
        if self.__srv_pr.size() == 0:
            print("No persons for now !")
            return
        for i in range(0, self.__srv_pr.size()):
            print(f"[{i + 1}]-> {self.__srv_pr.get_all()[i]}")
        print("-----------------------------------------------------")
        nb = int(input("Enter the number of the person you want to delete: "))
        if nb > self.__srv_pr.size() or nb < 1:
            print("Invalid Person Number !")
            return
        self.__srv_pr.delete(self.__srv_pr.get_all()[nb - 1].get_id_entity())

    def ui_update_person(self):
        if self.__srv_pr.size() == 0:
            print("No persons for now !")
            return
        for i in range(0, self.__srv_pr.size()):
            print(f"[{i + 1}]-> {self.__srv_pr.get_all()[i]}")
        print("-----------------------------------------------------")
        nb = int(input("Enter the number of the person you want to update: "))
        if nb > self.__srv_pr.size() or nb < 1:
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
            self.__srv_pr.update(name, surname, email, password, cnp, birthday, country, province, city, street, nr,
                                 self.__srv_pr.get_all()[nb - 1].get_id_entity())
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
                person = self.__srv_pr.get_all()[nb - 1]
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
                self.__srv_pr.update(name, surname, email, password, cnp, birthday, country, province, city, street, nr,
                                     person.get_id_entity())

    def ui_show_all_ps(self):
        for elem in self.__srv_pr.get_all():
            print(elem)

        # --{ FRIENDSHIP MENU }------------------------------------------------------------------------------------

    def ui_add_friendship(self):
        for i in range(0, self.__srv_pr.size()):
            print(f"[{i + 1}]-> {self.__srv_pr.get_all()[i]}")
        print("-----------------------------------------------------")
        pr1 = int(input("Enter the first person: "))
        pr2 = int(input("Enter the second person: "))
        if pr1 == pr2:
            print("A person cannot be friend with himself !")
            return
        pr1 = self.__srv_pr.get_all()[pr1 - 1].get_id_entity()
        pr2 = self.__srv_pr.get_all()[pr2 - 1].get_id_entity()
        self.__srv_fr.add(Friendship(0, pr1, pr2))

    def ui_del_friendship(self):
        pass

    def ui_update_friendship(self):
        pass

    def ui_show_all_fr(self):
        for elem in self.__srv_fr.get_all():
            person1 = (self.__srv_pr.find_by_id(elem.get_person1()).get_name() + " " +
                       self.__srv_pr.find_by_id(elem.get_person1()).get_surname())
            person2 = (self.__srv_pr.find_by_id(elem.get_person2()).get_name() + " " +
                       self.__srv_pr.find_by_id(elem.get_person2()).get_surname())
            print(person1 + " is friend with " + person2)
