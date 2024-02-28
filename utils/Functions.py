from domain.Personvalidator import PersonValidator
from service.ServicePerson import ServicePerson


def email_input(srv_pr: ServicePerson, validator: PersonValidator()):
    while True:
        email = input(" email:")
        try:
            while srv_pr.find_by_email(email) is not None or validator.validate_email(email) is False:
                print("Email already registered !\nPlease try again or type x to quit.")
                email = input(" email: ")
                if email == "x" or email == "X":
                    return None
        except Exception as e:
            print(e)
        print("Email is correct !")
        return email
