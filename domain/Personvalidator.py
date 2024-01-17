from domain.Person import Person


class PersonValidator:
    def validate(self, person: Person):
        errors = []
        if person.get_name() == "":
            errors.append("The person must have a name")
