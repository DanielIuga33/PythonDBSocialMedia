from domain.Person import Person
from repo.RepoPerson import RepoPerson


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

    def find_by_id(self, idc):
        if self.size() > 0:
            for elem in self.get_all():
                if int(elem.get_id()) == idc:
                    return elem
        return None

    def get_all(self):
        return self.__repo.get_all()

    def size(self):
        return self.__repo.size()
