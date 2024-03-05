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

    def __connect(self):
        try:
            mydb = psycopg2.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                port=25565,
                database="postgres"
            )
            return mydb
        except psycopg2.Error as e:
            try:
                mydb2 = psycopg2.connect(
                    host=self.__host,
                    user=self.__user,
                    password=self.__password,
                    port=5432,
                    database="PythonSocialMedia"
                )
                return mydb2
            except psycopg2.Error as y:
                print(f"Error connecting to {self.__host}:\n {e}")
                print(f"Error connecting to {self.__host}:\n {y}")

    def __read(self):
        result = []
        if self.__connect() is None:
            raise Exception("↓ Something is wrong with the connection! ↓")
        cursor = self.__connect().cursor()
        cursor.execute('SELECT id_person, name, surname, email, password, cnp, birthday,'
                       'country, province, city, street, nr FROM public."Person"')
        for elem in cursor.fetchall():
            result.append(Person(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], elem[7],
                                 elem[8], elem[9], elem[10], elem[11]))
        return result

    def __insert(self, elem: Person):
        conn = self.__connect()
        cursor = conn.cursor()
        sql = ('INSERT INTO public."Person" (id_person, name, surname, email, password, cnp, birthday, country,'
               ' province, city, street, nr) VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s)')
        person_data = (str(elem.get_id_entity()), elem.get_name(), elem.get_surname(), elem.get_email(),
                       elem.get_password(), elem.get_cnp(), elem.get_birthday(), elem.get_country(),
                       elem.get_province(), elem.get_city(), elem.get_street(), elem.get_nr())
        cursor.execute(sql, person_data)
        conn.commit()
        cursor.close()

    def __delete(self, elem: Person):
        conn = self.__connect()
        cursor = conn.cursor()
        sql = 'DELETE FROM public."Person" WHERE id_person = %s'

        cursor.execute(sql, (str(elem.get_id_entity()),))
        conn.commit()
        cursor.close()

    def __update(self, idp, p: Person):
        conn = self.__connect()
        cursor = conn.cursor()
        sql = ('UPDATE public."Person" SET name= %s,surname= %s, email= %s,password= %s, cnp= %s,birthday= %s,'
               'country= %s, province= %s, city= %s, street= %s, nr=%s WHERE id_person= %s')
        cursor.execute(sql, (p.get_name(), p.get_surname(), p.get_email(), p.get_password(), p.get_cnp(),
                             p.get_birthday(), p.get_country(), p.get_province(), p.get_city(), p.get_street(),
                             p.get_nr(), idp))
        conn.commit()
        cursor.close()

    def add(self, person: Person):
        self.__val.validate(person, "all")
        self.__repo.append(person)
        self.__insert(person)

    def delete(self, person: Person):
        self.__repo.remove(person)
        self.__delete(person)

    def update(self, idc, person: Person):
        self.__val.validate(person, "all")
        self.__update(idc, person)
        self.__repo = self.__read()

    def find_login(self, email, password):
        conn = self.__connect()
        cursor = conn.cursor()
        sql = ('SELECT id_person, name, surname, email, password, cnp, birthday,'
               'country, province, city, street, nr FROM public."Person" WHERE email= %s and password= %s LIMIT 1;')
        cursor.execute(sql, (email, password))
        elem = cursor.fetchone()
        if elem is None:
            return None
        else:
            return (Person(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], elem[7],
                           elem[8], elem[9], elem[10], elem[11]))

    def find_by_email(self, email: str):
        conn = self.__connect()
        cursor = conn.cursor()
        sql = ('SELECT id_person, name, surname, email, password, cnp, birthday,'
               'country, province, city, street, nr FROM public."Person" WHERE email= %s LIMIT 1;')
        cursor.execute(sql, (email,))
        elem = cursor.fetchone()
        if elem is None:
            return None
        else:
            return (Person(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], elem[7],
                           elem[8], elem[9], elem[10], elem[11]))

    def exists_by_email(self, email):
        conn = self.__connect()
        cursor = conn.cursor()
        sql = ('SELECT id_person, name, surname, email, password, cnp, birthday,'
               'country, province, city, street, nr FROM public."Person" WHERE email= %s LIMIT 1;')
        cursor.execute(sql, (email,))
        elem = cursor.fetchone()
        if elem is None:
            return False
        else:
            return True

    def find_by_id(self, idc):
        conn = self.__connect()
        cursor = conn.cursor()
        sql = ('SELECT id_person, name, surname, email, password, cnp, birthday,'
               'country, province, city, street, nr FROM public."Person" WHERE id_person= %s LIMIT 1;')
        cursor.execute(sql, (idc,))
        elem = cursor.fetchone()
        if elem is None:
            return None
        else:
            return (Person(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], elem[7],
                           elem[8], elem[9], elem[10], elem[11]))

    def get_all(self):
        return self.__repo

    def size(self):
        return len(self.__repo)
