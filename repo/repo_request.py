import psycopg2

import database_config
from domain.request import Request


class RepoRequest:
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
        cursor.execute('SELECT id_request, sender, receiver FROM public."Request"')
        for elem in cursor.fetchall():
            result.append(Request(elem[0], elem[1], elem[2]))
        return result

    def __insert(self, elem: Request):
        conn = self.connect()
        cursor = conn.cursor()
        sql = 'INSERT INTO public."Request" (sender, receiver) VALUES (%s, %s)'
        person_data = (str(elem.get_sender()), str(elem.get_receiver()))
        cursor.execute(sql, person_data)
        conn.commit()
        cursor.close()

    def __delete(self, elem: Request):
        conn = self.connect()
        cursor = conn.cursor()
        sql = 'DELETE FROM public."Request" WHERE id_request = %s'
        cursor.execute(sql, (str(elem.get_id_req()),))
        conn.commit()
        cursor.close()

    def delete_cascade(self, idp):
        conn = self.connect()
        cursor = conn.cursor()
        sql = 'DELETE FROM public."Request" WHERE sender = %s'
        sql1 = 'DELETE FROM public."Request" WHERE receiver = %s'

        cursor.execute(sql, (str(idp),))
        cursor.execute(sql1, (str(idp),))
        conn.commit()
        cursor.close()
        self.__repo = self.__read()

    def __update(self, idp, p: Request):
        conn = self.connect()
        cursor = conn.cursor()
        sql = 'UPDATE public."Request" SET sender= %s, receiver= %s WHERE id_request= %s'
        cursor.execute(sql, (p.get_sender(), p.get_receiver(), idp))
        conn.commit()
        cursor.close()

    def add(self, elem: Request):
        self.__repo.append(elem)
        self.__insert(elem)

    def delete(self, elem: Request):
        self.__repo.remove(elem)
        self.__delete(elem)

    def update(self, idc, elem: Request):
        self.__update(idc, elem)
        self.__repo = self.__read()

    def find_request(self, idp: Request):
        cursor = self.connect().cursor()
        sql = 'SELECT id_request FROM public."Request" WHERE sender = %s AND receiver = %s LIMIT 1;'
        cursor.execute(sql, (str(idp.get_sender()), str(idp.get_receiver())))
        lista = cursor.fetchall()
        if len(lista) > 0:
            return lista[0]
        else:
            return -1

    def get_all(self):
        return self.__repo

    def size(self):
        return len(self.__repo)
