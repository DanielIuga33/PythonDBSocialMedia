import uuid
from domain.Friendship import Friendship
import psycopg2


class RepoFriendship:
    def __init__(self, user, password):
        self.__host = "localhost"
        self.__user = user
        self.__password = password
        self.__repo = self.__read()

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
        cursor.execute('SELECT id_friendship, person1, person2 FROM public."Friendship"')
        for elem in cursor.fetchall():
            result.append(Friendship(elem[0], elem[1], elem[2]))
        return result

    def __insert(self, elem: Friendship):
        conn = self.__connect()
        cursor = conn.cursor()
        sql = 'INSERT INTO public."Friendship" (person1, person2) VALUES (%s, %s)'
        person_data = (str(elem.get_person1()), str(elem.get_person2()))
        cursor.execute(sql, person_data)
        conn.commit()
        cursor.close()

    def __delete(self, elem: Friendship):
        conn = self.__connect()
        cursor = conn.cursor()
        sql = 'DELETE FROM public."Friendship" WHERE id_friendship = %s'

        cursor.execute(sql, (str(elem.get_id_friendship()),))
        conn.commit()
        cursor.close()

    def __update(self, idp, p: Friendship):
        conn = self.__connect()
        cursor = conn.cursor()
        sql = 'UPDATE public."Friendship" SET person1= %s, person2= %s WHERE id_friendship= %s'
        cursor.execute(sql, (p.get_person1(), p.get_person2(), idp))
        conn.commit()
        cursor.close()

    def add(self, elem: Friendship):
        if self.find_friendship(elem) != -1:
            raise Exception('Friendship already exists !')
        self.__repo.append(elem)
        self.__insert(elem)

    def delete(self, elem: Friendship):
        if self.find_friendship(elem) == -1:
            raise Exception('Friendship does not exists !')
        self.__repo.remove(elem)
        self.__delete(elem)

    def update(self, idc, elem: Friendship):
        self.__update(idc, elem)
        self.__repo = self.__read()

    def find_friendship(self, idp: Friendship):
        cursor = self.__connect().cursor()
        sql = ('SELECT id_friendship FROM public."Friendship" WHERE (person1 = %s AND person2 = %s)'
               ' OR (person1 = %s AND person2 = %s) LIMIT 1;')
        cursor.execute(sql, (str(idp.get_person1()), str(idp.get_person2()),
                             str(idp.get_person2()), str(idp.get_person1())))
        if len(cursor.fetchall()) > 0:
            return cursor.fetchall()[0]
        else:
            return -1

    def get_all(self):
        return self.__repo

    def size(self):
        return len(self.__repo)
