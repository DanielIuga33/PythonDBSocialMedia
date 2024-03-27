from domain.friendship import Friendship
from domain.person import Person
from repo.repo_friendship import RepoFriendship


class ServiceFriendship:
    def __init__(self, repo_friendship: RepoFriendship):
        self.__repo = repo_friendship

    def add(self, person1, person2):
        self.__repo.add(Friendship(0, person1, person2, ""))

    def delete(self, fr: Friendship):
        self.__repo.delete(fr)

    def delete_cascade(self, id_person):
        self.__repo.delete_cascade(id_person)

    def find_friendship(self, person1, person2) -> Friendship:
        return self.__repo.find_friendship(person1, person2)

    def find_by_id(self, id_fr) -> Friendship:
        return self.__repo.find_by_id(id_fr)

    def size(self):
        return self.__repo.size()

    def get_all(self):
        return self.__repo.get_all()

    def add_conversation(self, sender: Person, id_fr, conversation):
        fr = self.find_by_id(id_fr)
        if fr.get_person2() == sender.get_id_person() or fr.get_text() == "":
            new_conv = fr.get_text() + f"{sender.get_name()} -> " + conversation + "\n"
            if fr.get_person2() == sender.get_id_person():
                fr.reverse_sender_receiver()
        else:
            new_conv = fr.get_text() + "       " + conversation + "\n"
        fr.set_text(new_conv)
        self.__repo.update(id_fr, fr)

    def delete_conversation(self, id_fr):
        fr = self.find_by_id(id_fr)
        fr.set_text("")
        self.__repo.update(id_fr, fr)

    def have_a_conversation(self, id_fr):
        fr = self.find_by_id(id_fr)
        if fr in self.get_all_friends_with_conversations():
            return True
        return False

    def get_all_friends_with_conversations(self):
        result = []
        for elem in self.get_all():
            if elem.get_text() != "":
                result.append(elem)
        return result
