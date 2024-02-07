from datetime import datetime

from domain.Entity import Entity


class Person(Entity):
    def __init__(self, id_entity, name, surname, email, password, cnp,
                 birthday, country, province, city, street, nr):
        super().__init__(id_entity)
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__password = password
        self.__cnp = cnp
        self.__birthday = birthday
        self.__country = country
        self.__province = province
        self.__city = city
        self.__street = street
        self.__nr = nr
        self.__age = datetime.now().year - datetime.strptime(self.__birthday, "%d/%m/%Y").year

    def __eq__(self, other):
        return (self.__name == other.__name and self.__surname == other.__surname
                and self.__email == other.__email and self.__password == other.__password
                and self.__cnp == other.__cnp and self.__birthday == other.__birthday
                and self.__country == other.__country and self.__province == other.__province
                and self.__city == other.__city and self.__street == other.__street
                and self.__nr == other.__nr)

    def __str__(self):
        string = ""
        for i in range(1, len(self.get_password())):
            string += "*"
        return (f"Name: {self.__name}, Surname: {self.__surname}, Email: {self.__email}, "
                f"Password: {self.get_password()[0]}{string}, Cnp: {self.__cnp}, Age: {self.__age}, "
                f"Country: {self.__country}, Province: {self.__province}, City: {self.__city}, "
                f"Street: {self.__street}, Nr: {self.__nr}")

    def under_age(self, age):
        return datetime.now().year - self.get_birthday().year < age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_cnp(self):
        return self.__cnp

    def get_birthday(self):
        birthday = datetime.strptime(self.__birthday, "%d/%m/%Y")
        return datetime.strftime(birthday, "%d/%m/%Y")

    def get_country(self):
        return self.__country

    def get_province(self):
        return self.__province

    def get_city(self):
        return self.__city

    def get_street(self):
        return self.__street

    def get_nr(self):
        return self.__nr

    def set_name(self, name):
        self.__name = name

    def set_surname(self, surname):
        self.__surname = surname

    def set_email(self, email):
        self.__email = email

    def set_password(self, pwd):
        self.__password = pwd

    def set_cnp(self, cnp):
        self.__cnp = cnp

    def set_birthday(self, brt):
        self.__birthday = brt

    def set_country(self, cty):
        self.__country = cty

    def set_province(self, prv):
        self.__province = prv

    def set_city(self, city):
        self.__city = city

    def set_street(self, street):
        self.__street = street

    def set_nr(self, nr):
        self.__nr = nr

