from domain.Personvalidator import PersonValidator
from service.ServicePerson import ServicePerson


def email_input(srv_pr: ServicePerson, validator: PersonValidator()):
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
                return None


def password_input(validator: PersonValidator()):
    password = input(" password:")
    while True:
        try:
            validator.validate_password(password)
            return password
        except Exception as e:
            print(f"{e}\nPlease try again or type x to quit.")
            password = input(" password:")
            if password == "x" or password == "X":
                return None
