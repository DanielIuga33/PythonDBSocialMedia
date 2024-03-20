from domain.person_validator import PersonValidator
from repo.repo_friendship import RepoFriendship
from service.service_person import ServicePerson


def string_input(tip):
    validator = PersonValidator()
    elem = input(f"Enter the person {tip}: ")
    match tip:
        case "name":
            while elem == "":
                print("\nPlease try again or type x to quit.")
                elem = input("Enter the person name: ")
                if elem == "x":
                    raise ValueError
        case "surname":
            while elem == "":
                print("\nPlease try again or type x to quit.")
                elem = input("Enter the person name: ")
                if elem == "x":
                    raise ValueError
        case "cnp":
            try:
                validator.validate(elem, "cnp")
            except ValueError as ve:
                print(ve)
                print("\nPlease try again or type x to quit.")
                elem = input("cnp: ")
                if elem == "x":
                    raise ValueError
        case "country":
            while validator.validate(elem, "country") is False:
                print("\nPlease try again or type x to quit.")
                elem = input("Enter the person name: ")
                if elem == "x":
                    raise ValueError
        case "province":
            while validator.validate(elem, "province") is False:
                print("\nPlease try again or type x to quit.")
                elem = input("Enter the person name: ")
                if elem == "x":
                    raise ValueError
        case "city":
            while validator.validate(elem, "city") is False:
                print("\nPlease try again or type x to quit.")
                elem = input("Enter the person name: ")
                if elem == "x":
                    raise ValueError
        case "street":
            while validator.validate(elem, "street") is False:
                print("\nPlease try again or type x to quit.")
                elem = input("Enter the person name: ")
                if elem == "x":
                    raise ValueError
        case "nr":
            while validator.validate(elem, "nr") is False:
                print("\nPlease try again or type x to quit.")
                elem = input("Enter the person name: ")
                if elem == "x":
                    raise ValueError
    return elem


def email_register(srv_pr: ServicePerson):
    validator = PersonValidator()
    email = input(" email:")
    while True:
        try:
            validator.validate_email(email)
            if srv_pr.exists_by_email(email) is True:
                raise Exception("Email already registered !")
            return email
        except Exception as e:
            print(f"{e}\nPlease try again or type x to quit.")
            email = input(" email: ")
            if email == "x" or email == "X":
                raise ValueError


def email_login(srv_pr: ServicePerson):
    email = input(" email:")
    while srv_pr.exists_by_email(email) is False:
        print("There is no account with this email ! \nPlease try again or type x to quit")
        email = input(" email:")
        if email == "x":
            raise ValueError
    return email


def password_login(srv_pr: ServicePerson):
    password = input(" password:")
    while srv_pr.exists_by_password(password) is False:
        print("Invalid email \nPlease try again or type x to quit")
        password = input(" password:")
        if password == "x":
            raise ValueError
    return password


def password_register():
    validator = PersonValidator()
    password = input(" password:")
    while True:
        try:
            validator.validate_password(password)
            return password
        except Exception as e:
            print(f"{e}\nPlease try again or type x to quit.")
            password = input(" password:")
            if password == "x" or password == "X":
                raise ValueError


def delete_cascade(idp, repo_friendship: RepoFriendship, who):
    if who == "person":
        repo_friendship.delete_cascade(idp)
