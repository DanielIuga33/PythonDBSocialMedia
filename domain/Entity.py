from uuid import UUID


class Entity:
    def __init__(self, id_entity: UUID):
        self.__id_entity = id_entity

    def get_id_entity(self):
        return self.__id_entity

    def set_id_entity(self, id_entity: UUID):
        self.__id_entity = id_entity


