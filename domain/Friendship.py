class Friendship:
    def __init__(self, id_friendship, person1, person2):
        self.__id_friendship = id_friendship
        self.__person1 = person1
        self.__person2 = person2

    def get_id_friendship(self):
        return self.__id_friendship

    def get_person1(self):
        return self.__person1

    def get_person2(self):
        return self.__person2

    def set_id_friendship(self, id_friendship):
        self.__id_friendship = id_friendship

    def set_person1(self, person1):
        self.__person1 = person1

    def set_person2(self, person2):
        self.__person2 = person2
