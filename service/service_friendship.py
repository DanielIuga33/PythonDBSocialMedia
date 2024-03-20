from domain.friendship import Friendship
from repo.repo_friendship import RepoFriendship


class ServiceFriendship:
    def __init__(self, repo_friendship: RepoFriendship):
        self.__repo = repo_friendship

    def add(self, person1, person2):
        self.__repo.add(Friendship(0, person1, person2, ""))

    def delete(self, fr: Friendship):
        self.__repo.delete(fr)

    def find_friendship(self, person1, person2):
        return self.__repo.find_friendship(person1, person2)

    def size(self):
        return self.__repo.size()

    def get_all(self):
        return self.__repo.get_all()
