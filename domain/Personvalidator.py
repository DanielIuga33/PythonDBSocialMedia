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
            case "all":
                return self.__validate_all(elem)

    def __validate_all(self, person: Person) -> bool:
        try:
            if (self.validate(person.get_name(), "name")
                    or self.validate(person.get_surname(), "surname")
                    or self.validate(person.get_cnp(), "cnp")
                    or self.validate(person.get_birthday(), "birthday")
                    or self.validate(person.get_country(), "country")
                    or self.validate(person.get_province(), "province")
                    or self.validate(person.get_city(), "city")
                    or self.validate(person.get_street(), "street")
                    or self.validate(person.get_nr(), "nr") is False):
                return False
            self.validate_email(person.get_email())
            self.validate_password(person.get_password())
        except Exception as e:
            print(e)
            return False

    def validate_email(self, email):
        errors = ""
        if len(email) < 3:
            errors += "Invalid email size !"
        if ((email[len(email) - 1] != "m" or email[len(email) - 2] != "o" or
             email[len(email) - 3] != "c") and (email[len(email) - 1] != "o" or
                                                email[len(email) - 2] != "r")):
            if errors:
                errors += "\n"
            errors += "Invalid email (it needs to end with '.com' or .ro)!"
        if "@" not in email:
            if errors:
                errors += "\n"
            errors += "The email must contain '@' !"
        name_part = email.split("@")[0]
        if ("0" not in name_part and "1" not in name_part and "2" not in name_part and
                "3" not in name_part and "4" not in name_part and "5" not in name_part and
                "6" not in name_part and "7" not in name_part and "8" not in name_part and
                "9" not in name_part):
            if errors:
                errors += "\n"
            errors += "Email must contain numbers !"
        if errors:
            raise Exception(errors)

    def validate_password(self, password):
        errors = ""
        if len(password) < 8 or len(password) > 16:
            errors += "Password must be between 8 and 16 characters !"
        if ("0" not in password and "1" not in password and "2" not in password and
                "3" not in password and "4" not in password and "5" not in password and
                "6" not in password and "7" not in password and "8" not in password and
                "9" not in password):
            if errors:
                errors += "\n"
            errors += "Password must contain numbers !"

        if password == password.lower():
            if errors:
                errors += "\n"
            errors += "Password must contain at least one uppercase letter !"
        if errors:
            raise Exception(errors)
