import psycopg2
import database_config
from domain.notification import Notification


class RepoNotification:
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
        cursor.execute('SELECT id_notification, person, tip, message FROM public."Notification"')
        for elem in cursor.fetchall():
            result.append(Notification(elem[0], elem[1], elem[2], elem[3]))
        return result

    def __insert(self, elem: Notification):
        conn = self.connect()
        cursor = conn.cursor()
        sql = 'INSERT INTO public."Notification" (person, tip, message) VALUES (%s, %s, %s)'
        person_data = (str(elem.get_person()), elem.get_tip(), elem.get_message())
        cursor.execute(sql, person_data)
        conn.commit()
        cursor.close()

    def __delete(self, elem: Notification):
        conn = self.connect()
        cursor = conn.cursor()
        sql = 'DELETE FROM public."Notification" WHERE id_notification = %s'

        cursor.execute(sql, (str(elem.get_id_notification()),))
        conn.commit()
        cursor.close()

    def delete_cascade(self, idp):
        conn = self.connect()
        cursor = conn.cursor()
        sql = 'DELETE FROM public."Notification" WHERE person = %s'

        cursor.execute(sql, (str(idp),))
        conn.commit()
        cursor.close()
        self.__repo = self.__read()

    def __update(self, idp, p: Notification):
        conn = self.connect()
        cursor = conn.cursor()
        sql = 'UPDATE public."Notification" SET person= %s, tip= %s, message = %s WHERE id_notification= %s'
        cursor.execute(sql, (p.get_id_notification(), p.get_person(), p.get_message(), idp))
        conn.commit()
        cursor.close()

    def add(self, elem: Notification):
        #if self.__find_notification(elem) != -1:
            #raise Exception('Notification already exists !')
        self.__repo.append(elem)
        self.__insert(elem)

    def delete(self, elem: Notification):
        if self.__find_notification(elem) == -1:
            raise Exception('Notification does not exists !')
        self.__repo.remove(elem)
        self.__delete(elem)

    def update(self, idc, elem: Notification):
        self.__update(idc, elem)
        self.__repo = self.__read()

    def find_notifications(self, id_person):
        cursor = self.connect().cursor()
        sql = 'SELECT * FROM public."Notification" WHERE person = %s'
        cursor.execute(sql, (str(id_person),))
        lista = cursor.fetchall()
        if lista is None:
            return -1
        elif len(lista) > 0:
            return lista[0]
        else:
            return -1

    def find_notification(self, idn):
        cursor = self.connect().cursor()
        sql1 = 'SELECT id_notification FROM public."Notification" WHERE id_notification = %s LIMIT 1;'
        cursor.execute(sql1, (str(idn.get_id_notification()),))
        lista = cursor.fetchone()
        if lista is None:
            return -1
        elif len(lista) == 0:
            return -1
        else:
            return 0

    def get_all(self):
        return self.__repo

    def size(self):
        return len(self.__repo)
