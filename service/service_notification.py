from domain.notification import Notification
from repo.repo_notification import RepoNotification


class ServiceNotification:
    def __init__(self, repo: RepoNotification):
        self.__repo = repo

    def add(self, idp, text):
        notification = Notification("0", idp, "unread", text)
        self.__repo.add(notification)

    def delete(self, notification):
        self.__repo.delete(notification)

    def update(self, idn, new_notification):
        self.__repo.update(idn, new_notification)

    def find_notifications(self, id_person):
        return self.__repo.find_notifications(id_person)

    def all_notifications_for_a_person(self, id_person):
        result = []
        for elem in self.get_all():
            if elem.get_person() == id_person:
                result.append(elem)
        return result

    def get_unread_notifications(self, id_person):
        result = []
        for elem in self.get_all():
            if elem.get_person() == id_person and elem.get_tip() == "unread":
                result.append(elem)
        return result, len(result)

    def get_read_notifications(self, id_person):
        result = []
        for elem in self.get_all():
            if elem.get_person() == id_person and elem.get_tip() == "unread":
                result.append(elem)
        return result, len(result)

    def set_notification_to_read(self, idn):
        ntf = self.__repo.find_notifications(idn)
        ntf.set_tip("read")
        self.__repo.update(idn, ntf)

    def get_all(self):
        return self.__repo.get_all()

    def size(self):
        return self.__repo.size()
