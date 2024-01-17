import psycopg2

from domain.Person import Person
from domain.Personvalidator import PersonValidator


class RepoPerson:
    def __init__(self, user, password):
        self.__host = "localhost"
        self.__user = user
        self.__password = password
        self.__repo = self.__read()
        self.__val = PersonValidator()
        self.__cursor = self.__connect()

    def __connect(self):
        try:
            mydb = psycopg2.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                port=25565
            )
            return mydb.cursor()
        except psycopg2.Error as e:
            print(f"Error connecting to {self.__host}:\n {e}")

    def __read(self):
        result = []
        self.__cursor.execute('SELECT id_person, name, surname, email, password, cnp, birthday,'
                              'country, province, city, street, nr FROM public."Person"')
        for elem in self.__cursor.fetchall():
            result.append(Person(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], elem[7],
                                 elem[8], elem[9], elem[10], elem[11]))
        return result

    def __insert(self, elem: Person):
        self.__cursor.execute(f'INSERT INTO public."Person"(id_person, name, surname, email,'
                              f' password, cnp, birthday, country, province, city, street, nr)'
                              f' VALUES ({elem.get_id_entity()},'
                              f' {elem.get_name()}, {elem.get_surname()},'
                              f' {elem.get_email()}, {elem.get_password()},'
                              f' {elem.get_cnp()}, {elem.get_birthday()},'
                              f' {elem.get_country()}, {elem.get_province()},'
                              f' {elem.get_city()}, {elem.get_street()},'
                              f' {elem.get_nr()});')

    def __delete(self, elem: Person):
        self.__cursor.execute(f'DELETE FROM public."Person"'
                              f' WHERE id_person = {elem.get_id_entity()};')

    def __update(self, idp, p: Person):
        self.__cursor.execute(f'UPDATE public."Person" SET id_person={idp}, name={p.get_name()}, '
                              f'surname={p.get_surname()}, email={p.get_email()},'
                              f' password={p.get_password()}, cnp={p.get_cnp()},'
                              f' birthday={p.get_birthday()}, country={p.get_country()}, '
                              f'province={p.get_province()}, city={p.get_city()}, '
                              f'street={p.get_street()}, nr={p.get_nr()}'
                              f'WHERE id_person={idp};')

    def add(self, person: Person):
        self.__val.validate(person)
        self.__repo.append(person)
        self.__insert(person)

    def delete(self, person: Person):
        self.__repo.remove(person)
        self.__delete(person)

    def update(self, idc, person: Person):
        self.__update(idc, person)
        self.__repo = self.__read()

    def get_all(self):
        return self.__repo

    def size(self):
        return len(self.__repo)

