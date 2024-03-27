class Notification:
    def __init__(self, id_notification, id_person, tip, message, data):
        self.__id_notification = id_notification
        self.__person = id_person
        self.__tip = tip
        self.__message = message
        self.__data = data

    def get_id_notification(self):
        return self.__id_notification

    def get_person(self):
        return self.__person

    def get_tip(self):
        return self.__tip

    def get_message(self):
        return self.__message

    def get_data(self):
        return self.__data

    def set_id_notification(self, id_notification):
        self.__id_notification = id_notification

    def set_person(self, id_person):
        self.__person = id_person

    def set_tip(self, tip):
        self.__tip = tip

    def set_message(self, message):
        self.__message = message

    def set_data(self, data):
        self.__data = data
