import mysql.connector


class RepoPerson:
    def __init__(self, host, user, password, database):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

    def __connect(self):
        try:
            mydb = mysql.connector.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__database
            )
            return mydb.cursor()
        except mysql.connector.Error as e:
            print(f"Error connecting to {self.__host}:\n {e}")

    def __read(self):
        cursor = self.__connect()
        cursor.execute("SELECT * FROM Persons")