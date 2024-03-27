import uuid

from domain.request import Request
from utils.prints import *
from utils.functions import *


class Admin:
    def __init__(self, srv_pr, srv_fr, srv_req, srv_ntf):
        self.__srv_pr = srv_pr
        self.__srv_fr = srv_fr
        self.__srv_req = srv_req
        self.__srv_ntf = srv_ntf
        self.__validator = PersonValidator()

    def run(self):
        while True:
            print_admin_main_menu()
            choice = input("Give here your choice: ")
            match choice:
                case "1":
                    self.person_menu()
                case "2":
                    self.request_menu()
                case "3":
                    self.friendship_menu()
                case "4":
                    self.conversation_menu()
                case "5":
                    self.notification_menu()
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

    def request_menu(self):
        if self.__srv_pr.size() <= 1:
            print("You have to add at least 2 persons !")
            return
        while True:
            print_admin_request_menu()
            choice = input("Give here your choice: ")
            match choice:
                case "1":
                    self.ui_add_request()
                case "2":
                    self.ui_del_request()
                case "3":
                    self.ui_update_request()
                case "a":
                    self.ui_show_all_req()
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

    def conversation_menu(self):
        if self.__srv_fr.size() == 0:
            print("You have to add at least 1 Friendship !")
            return
        while True:
            print_admin_conversation_menu()
            choice = input("Give here your choice: ")
            match choice:
                case "1":
                    self.ui_add_conversation()
                case "2":
                    self.ui_del_conversation()
                case "3":
                    self.ui_update_conversation()
                case "a":
                    self.ui_show_all_cnv()
                case "x":
                    break
                case _:
                    print("Invalid choice !")

    def notification_menu(self):
        if self.__srv_pr.size() == 0:
            print("You have to add at least 1 persons !")
            return
        while True:
            print_admin_notification_menu()
            choice = input("Give here your choice: ")
            match choice:
                case "1":
                    self.ui_add_notification()
                case "2":
                    self.ui_del_notification()
                case "3":
                    self.ui_update_notification()
                case "a":
                    self.ui_show_all_ntf()
                case "x":
                    break
                case _:
                    print("Invalid choice !")

        # --{ PERSON MENU }----------------------------------------------------------------------------------------

    def ui_add_person(self):
        try:
            idc = uuid.uuid4()
            name = string_input("name")
            surname = string_input("surname")
            email = email_register(self.__srv_pr)
            password = password_register()
            cnp = string_input("cnp")
            birthday = input("Enter the person birthday(dd/mm/yyyy format): ")
            country = input("*Enter the country of the person: ")
            province = input("*Enter the province of the person: ")
            city = input("*Enter the city/village of the person: ")
            street = input("*Enter the street: ")
            nr = input("*Enter the number: ")
            self.__srv_pr.add(idc, name, surname, email, password, cnp, birthday, country, province, city, street, nr)
            print("Person added successfully !")
        except ValueError as e:
            print(e)

    def ui_del_person(self):
        if self.__srv_pr.size() == 0:
            print("No persons for now !")
            return
        try:
            for i in range(0, self.__srv_pr.size()):
                print(f"[{i + 1}]-> {self.__srv_pr.get_all()[i]}")
            print("-----------------------------------------------------")
            nb = int(input("Enter the number of the person you want to delete: "))
            if nb > self.__srv_pr.size() or nb < 1:
                print("Invalid Person Number !")
                return
            self.__srv_fr.delete_cascade(self.__srv_pr.get_all()[nb - 1].get_id_person())
            self.__srv_pr.delete(self.__srv_pr.get_all()[nb - 1].get_id_person())
            print("Person deleted successfully !")
        except Exception as e:
            print(e)

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
                                 self.__srv_pr.get_all()[nb - 1].get_id_person())
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
                                     person.get_id_person())
                print("Person updated successfully !")

    def ui_show_all_ps(self):
        for elem in self.__srv_pr.get_all():
            print(elem)
        # --{ REQUEST MENU }---------------------------------------------------------------------------------------

    def ui_add_request(self):
        try:
            for i in range(0, self.__srv_pr.size()):
                print(f"[{i + 1}]-> {self.__srv_pr.get_all()[i]}")
            print("-----------------------------------------------------")
            pr1 = int(input("Enter the first person: "))
            pr2 = int(input("Enter the second person: "))
            if pr1 == pr2:
                print("A person cannot request himself !")
                return
            pr1 = self.__srv_pr.get_all()[pr1 - 1].get_id_person()
            pr2 = self.__srv_pr.get_all()[pr2 - 1].get_id_person()
            self.__srv_req.add(Request(0, pr1, pr2))
            print("Request added successfully !")
        except Exception as e:
            print(e)

    def ui_del_request(self):
        if self.__srv_req.size() == 0:
            print("There are no requests yet !")
            return
        try:
            for i in range(0, self.__srv_req.size()):
                person1 = (self.__srv_pr.find_by_id(self.__srv_req.get_all()[i].get_sender()).get_name() + " " +
                           self.__srv_pr.find_by_id(self.__srv_req.get_all()[i].get_sender()).get_surname())
                person2 = (self.__srv_pr.find_by_id(self.__srv_req.get_all()[i].get_receiver()).get_name() + " " +
                           self.__srv_pr.find_by_id(self.__srv_req.get_all()[i].get_receiver()).get_surname())
                print(f"[{i + 1}]-> {person1 + " wants to be friend with " + person2}")
            nb = int(input("Enter the number of request you want to delete: "))
            if nb > self.__srv_req.size() or nb < 1:
                print("Invalid Request Number !")
                return
            self.__srv_req.delete(self.__srv_req.get_all()[nb - 1])
            print("Request deleted successfully!")
        except Exception as e:
            print(e)

    def ui_update_request(self):
        pass

    def ui_show_all_req(self):
        if self.__srv_req.size() == 0:
            print("No requests for now..")
            return
        for elem in self.__srv_req.get_all():
            person1 = (self.__srv_pr.find_by_id(elem.get_sender()).get_name() + " " +
                       self.__srv_pr.find_by_id(elem.get_sender()).get_surname())
            person2 = (self.__srv_pr.find_by_id(elem.get_receiver()).get_name() + " " +
                       self.__srv_pr.find_by_id(elem.get_receiver()).get_surname())
            print(person1 + " wants to be friend with " + person2)

        # --{ FRIENDSHIP MENU }------------------------------------------------------------------------------------

    def ui_add_friendship(self):
        try:
            for i in range(0, self.__srv_pr.size()):
                print(f"[{i + 1}]-> {self.__srv_pr.get_all()[i]}")
            print("-----------------------------------------------------")
            pr1 = int(input("Enter the first person: "))
            if pr1 > self.__srv_pr.size() or pr1 < 1:
                print("Invalid Person Number !")
                return
            pr2 = int(input("Enter the second person: "))
            if pr2 > self.__srv_pr.size() or pr2 < 1:
                print("Invalid Person Number !")
                return
            if pr1 == pr2:
                print("A person cannot be friend with himself !")
                return
            pr1 = self.__srv_pr.get_all()[pr1 - 1].get_id_person()
            pr2 = self.__srv_pr.get_all()[pr2 - 1].get_id_person()
            self.__srv_fr.add(pr1, pr2)
            print("Friendship added successfully !")
        except Exception as e:
            print(e)

    def ui_del_friendship(self):
        if self.__srv_fr.size() == 0:
            print("There are no friendships yet !")
            return
        try:
            for i in range(0, self.__srv_fr.size()):
                person1 = (self.__srv_pr.find_by_id(self.__srv_fr.get_all()[i].get_person1()).get_name() + " " +
                           self.__srv_pr.find_by_id(self.__srv_fr.get_all()[i].get_person1()).get_surname())
                person2 = (self.__srv_pr.find_by_id(self.__srv_fr.get_all()[i].get_person2()).get_name() + " " +
                           self.__srv_pr.find_by_id(self.__srv_fr.get_all()[i].get_person2()).get_surname())
                print(f"[{i + 1}]-> {person1 + " is friend with " + person2}")
            nb = int(input("Enter the number of the friendship you want to delete: "))
            if nb > self.__srv_pr.size() or nb < 1:
                print("Invalid Friendship Number !")
                return
            self.__srv_fr.delete(self.__srv_fr.get_all()[nb - 1])
            print("Friendship deleted successfully !")
        except Exception as e:
            print(e)

    def ui_update_friendship(self):
        pass

    def ui_show_all_fr(self):
        if self.__srv_fr.size() == 0:
            print("No friendships for now..")
            return
        for elem in self.__srv_fr.get_all():
            person1 = (self.__srv_pr.find_by_id(elem.get_person1()).get_name() + " " +
                       self.__srv_pr.find_by_id(elem.get_person1()).get_surname())
            person2 = (self.__srv_pr.find_by_id(elem.get_person2()).get_name() + " " +
                       self.__srv_pr.find_by_id(elem.get_person2()).get_surname())
            print(person1 + " is friend with " + person2)

    # --{ CONVERSATION MENU }----------------------------------------------------------------------------------

    def ui_add_conversation(self):
        try:
            for i in range(0, self.__srv_pr.size()):
                print(f"[{i + 1}]-> {self.__srv_pr.get_all()[i]}")
            print("-----------------------------------------------------")
            sender = int(input("Enter the person who sends the message: "))
            if sender > self.__srv_pr.size() or sender < 1:
                print("Invalid Person Number !")
                return
            receiver = int(input("Enter the person who receives the message: "))
            if receiver > self.__srv_pr.size() or receiver < 1:
                print("Invalid Person Number !")
                return
            if sender == receiver:
                print("A person cannot message himself !")
                return
            sender = self.__srv_pr.get_all()[sender - 1].get_id_person()
            receiver = self.__srv_pr.get_all()[receiver - 1].get_id_person()
            if self.__srv_fr.find_friendship(sender, receiver) == -1:
                print(f" {sender.get_name()} and {receiver.get_name()} need to be friends\n"
                      f"in order to have a conversation !")
                return
            text = input("Enter the message: ")
            friendship = self.__srv_fr.find_friendship(sender, receiver)
            self.__srv_fr.add_conversation(self.__srv_pr.find_by_id(sender), friendship, text)
        except Exception as e:
            print(e)

    def ui_del_conversation(self):
        if len(self.__srv_fr.get_all_friends_with_conversations()) == 0:
            print("No conversations yet !")
            return
        for i in range(0, len(self.__srv_fr.get_all_friends_with_conversations())):
            pr1 = self.__srv_pr.find_by_id(
                self.__srv_fr.find_by_id(self.__srv_fr.get_all_friends_with_conversations()[i].get_id_friendship())
                .get_person1()).get_surname()
            pr2 = self.__srv_pr.find_by_id(
                self.__srv_fr.find_by_id(self.__srv_fr.get_all_friends_with_conversations()[i].get_id_friendship())
                .get_person2()).get_surname()
            print(f"[{i + 1}]-> {pr1} and {pr2} have a conversation")
        nb = int(input("Enter the number of the conversation you want to delete: "))
        if nb > len(self.__srv_fr.get_all_friends_with_conversations()) or nb < 1:
            print("Invalid Conversation Number !")
            return
        self.__srv_fr.delete_conversation(self.__srv_fr.get_all_friends_with_conversations()[nb - 1].
                                          get_id_friendship())
        print("Conversation deleted successfully !")

    def ui_update_conversation(self):
        pass

    def ui_show_all_cnv(self):
        if len(self.__srv_fr.get_all_friends_with_conversations()) == 0:
            print("No conversations yet !")
            return
        for elem in self.__srv_fr.get_all_friends_with_conversations():
            print(f"{self.__srv_pr.find_by_id(self.__srv_fr.find_by_id(elem.get_id_friendship()).get_person1()).
                  get_surname()} has a conversation with "
                  f"{self.__srv_pr.find_by_id(self.__srv_fr.find_by_id(elem.get_id_friendship()).
                                              get_person2()).get_surname()}")
            print(elem.get_text())

    # --{ NOTIFICATION MENU }----------------------------------------------------------------------------------
    def ui_add_notification(self):
        for i in range(0, self.__srv_pr.size()):
            print(f"[{i + 1}]-> {self.__srv_pr.get_all()[i]}")
        print("-----------------------------------------------------")
        pr = int(input("Enter the person you want to add a notification: "))
        if pr > self.__srv_pr.size() or pr < 1:
            print("Invalid Person Number !")
            return
        person = self.__srv_pr.get_all()[pr - 1].get_id_person()
        msg = input("Enter the notification message you want to send: ")
        self.__srv_ntf.add(person, msg)
        print("Notification added successfully !")

    def ui_del_notification(self):
        if self.__srv_ntf.size() == 0:
            print("No notifications yet !")

    def ui_update_notification(self):
        pass

    def ui_show_all_ntf(self):
        for elem in self.__srv_ntf.get_all():
            print(f"{self.__srv_pr.find_by_id(elem.get_person()).get_surname()}:  {elem.get_message()}")
