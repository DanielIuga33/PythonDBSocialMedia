import psycopg2
import database_config
from domain.friendship import Friendship


class RepoFriendship:
    def __init__(self):
        self.__repo = self.__read()

    @staticmethod
    def connect():
        try:
            mydb2 = psycopg2.connect(
                host=database_config.host,
                user=database_config.user,
                password=database_config.password,
                port=database_config.port,
                database=database_config.database
            )
            return mydb2
        except psycopg2.Error as y:
            print(f"Error connecting to database:\n {y}")
            return None

    def __read(self):
        result = []
        if self.connect() is None:
            raise Exception("↓ Something is wrong with the connection! ↓")
        cursor = self.connect().cursor()
        cursor.execute('SELECT id_friendship, person1, person2, conversation FROM public."Friendship"')
        for elem in cursor.fetchall():
            result.append(Friendship(elem[0], elem[1], elem[2], elem[3]))
        return result

    def __insert(self, elem: Friendship):
        conn = self.connect()
        cursor = conn.cursor()
        sql = 'INSERT INTO public."Friendship" (person1, person2, conversation) VALUES (%s, %s, %s)'
        person_data = (str(elem.get_person1()), str(elem.get_person2()), elem.get_text())
        cursor.execute(sql, person_data)
        conn.commit()
        cursor.close()

    def __delete(self, elem: Friendship):
        conn = self.connect()
        cursor = conn.cursor()
        sql = 'DELETE FROM public."Friendship" WHERE id_friendship = %s'

        cursor.execute(sql, (str(elem.get_id_friendship()),))
        conn.commit()
        cursor.close()

    def delete_cascade(self, idp):
        conn = self.connect()
        cursor = conn.cursor()
        sql = 'DELETE FROM public."Friendship" WHERE person1 = %s'
        sql1 = 'DELETE FROM public."Friendship" WHERE person2 = %s'

        cursor.execute(sql, (str(idp),))
        cursor.execute(sql1, (str(idp),))
        conn.commit()
        cursor.close()
        self.__repo = self.__read()

    def __update(self, idp, p: Friendship):
        conn = self.connect()
        cursor = conn.cursor()
        sql = 'UPDATE public."Friendship" SET person1= %s, person2= %s, conversation = %s WHERE id_friendship= %s'
        cursor.execute(sql, (p.get_person1(), p.get_person2(), p.get_text(), idp))
        conn.commit()
        cursor.close()

    def add(self, elem: Friendship):
        if self.find_friendship(elem.get_person1(), elem.get_person2()) != -1:
            raise Exception('Friendship already exists !')
        self.__repo.append(elem)
        self.__insert(elem)

    def delete(self, elem: Friendship):
        if self.find_friendship(elem.get_person1(), elem.get_person2()) == -1:
            raise Exception('Friendship does not exists !')
        self.__repo.remove(elem)
        self.__delete(elem)

    def update(self, idc, elem: Friendship):
        self.__update(idc, elem)
        self.__repo = self.__read()

    def find_friendship(self, id_person1, id_person2):
        cursor = self.connect().cursor()
        sql = ('SELECT id_friendship FROM public."Friendship" WHERE (person1 = %s AND person2 = %s)'
               ' OR (person1 = %s AND person2 = %s) LIMIT 1;')
        cursor.execute(sql, (str(id_person1), str(id_person2),
                             str(id_person2), str(id_person1)))
        lista = cursor.fetchone()
        if lista is None:
            return -1
        elif len(lista) > 0:
            return lista[0]
        else:
            return -1

    def find_by_id(self, idp):
        cursor = self.connect().cursor()
        sql1 = 'SELECT person1, person2, conversation FROM public."Friendship" WHERE id_friendship = %s LIMIT 1;'
        # sql2 = 'SELECT person2 FROM public."Friendship" WHERE id_friendship = %s LIMIT 1;'
        cursor.execute(sql1, (str(idp),))
        person1, person2, conversation = cursor.fetchall()
        # cursor.execute(sql2, (str(idp),))
        # person2 = cursor.fetchone()[0]
        return Friendship(idp, person1, person2, conversation)

    def get_all(self):
        return self.__repo

    def size(self):
        return len(self.__repo)
