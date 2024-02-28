from domain.Person import Person


class PersonValidator:
    def validate(self, elem, att):
        match att:
            case "name":
                if elem == "":
                    print("You must complete the name field before proceeding !")
                    return False
            case "surname":
                if elem == "":
                    print("You must complete the surname field before proceeding !")
                    return False
            case "cnp":
                if elem.isdigit() is False:
                    print("CNP must contain only numbers !")
                    return False
                if len(elem) != 13:
                    print("Invalid CNP !")
                    return False
            case "country":
                if elem == "":
                    print("You must complete the name field before proceeding !")
                    return False
            case "province":
                if elem == "":
                    print("You must complete the name field before proceeding !")
                    return False
            case "city":
                if elem == "":
                    print("You must complete the name field before proceeding !")
                    return False
            case "street":
                if elem == "":
                    print("You must complete the name field before proceeding !")
                    return False

        # self.__email = email
        # self.__password = password
        # self.__cnp = cnp
        # self.__birthday = birthday
        # self.__country = country
        # self.__province = province
        # self.__city = city
        # self.__street = street
        # self.__nr = nr
        # self.__age = datetime.now().year - datetime.strptime(self.__birthday, "%d/%m/%Y").year

    def validate_email(self, email):
        if len(email) < 3:
            raise Exception("Invalid email !")
        if (email[len(email) - 1] != "m" or email[len(email) - 2] != "o" or
                email[len(email) - 3] != "c" and email[len(email) - 1] != "o" or
                email[len(email) - 2] != "r"):
            raise Exception("Invalid email !")
        if "@" not in email:
            raise Exception("The email must contain '@' !")
        name_part = email.split("@")[0]
        if ("0" not in name_part and "1" not in name_part and "2" not in name_part and
                "3" not in name_part and "4" not in name_part and "5" not in name_part and
                "6" not in name_part and "7" not in name_part and "8" not in name_part and
                "9" not in name_part):
            raise Exception("Email must contain numbers !")
        return True

    def validate_password(self, password):
        if len(password) < 8 or len(password) > 16:
            raise Exception("Password must be between 8 and 16 characters !")
        if ("0" not in password and "1" not in password and "2" not in password and
                "3" not in password and "4" not in password and "5" not in password and
                "6" not in password and "7" not in password and "8" not in password and
                "9" not in password):
            raise Exception("Password must contain numbers !")
        if password == password.upper():
            raise Exception("Password must contain at least one uppercase letter !")


