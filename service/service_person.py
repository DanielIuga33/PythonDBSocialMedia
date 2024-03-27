from domain.person import Person
from repo.repo_person import RepoPerson


class ServicePerson:
    def __init__(self, repo: RepoPerson):
        self.__repo = repo

    def add(self, idc, name, surname, email, password, cnp, birthday, country, province, city, street, nr):
        self.__repo.add(Person(idc, name, surname, email, password, cnp,
                               birthday, country, province, city, street, nr))

    def delete(self, idc):
        if self.find_by_id(idc) is not None:
            self.__repo.delete(self.find_by_id(idc))
        else:
            raise ValueError("There is no person with this id !")

    def update(self, name, surname, email, password, cnp, birthday, country, province, city, street, nr, idc):
        self.__repo.update(idc, Person(idc, name, surname, email, password, cnp, birthday, country, province,
                                       city, street, nr))

    def find_by_id(self, idc):
        return self.__repo.find_by_id(idc)

    def find_login(self, email, password):
        return self.__repo.find_login(email, password)

    def find_by_email(self, email):
        return self.__repo.find_by_email(email)

    def exists_by_password(self, password) -> bool:
        return self.__repo.exists_by_password(password)

    def exists_by_email(self, email):
        return self.__repo.exists_by_email(email)

    def get_all(self):
        return self.__repo.get_all()

    def size(self):
        return self.__repo.size()
