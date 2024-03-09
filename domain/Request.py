class Request:
    def __init__(self, id_req, sender, receiver):
        self.__id_req = id_req
        self.__sender = sender
        self.__receiver = receiver

    def get_id_req(self):
        return self.__id_req

    def get_sender(self):
        return self.__sender

    def get_receiver(self):
        return self.__receiver

    def set_id_req(self, id_req):
        self.__id_req = id_req

    def set_sender(self, sender):
        self.__sender = sender

    def set_receiver(self, receiver):
        self.__receiver = receiver
