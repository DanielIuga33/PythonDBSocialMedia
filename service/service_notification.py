from repo.repo_notification import RepoNotification


class ServiceNotification:
    def __init__(self, repo: RepoNotification):
        self.__repo = repo

    def add(self, notification):
        self.__repo.add(notification)

    def delete(self, notification):
        self.__repo.delete(notification)

    def update(self, idn, new_notification):
        self.__repo.update(idn, new_notification)

    def find_notifications(self, id_person):
        return self.__repo.find_notifications(id_person)

    def get_all(self):
        return self.__repo.get_all()

    def size(self):
        return self.__repo.size()
