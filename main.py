from repo.repo_friendship import RepoFriendship
from repo.repo_notification import RepoNotification
from repo.repo_person import RepoPerson
from repo.repo_request import RepoRequest
from service.service_friendship import ServiceFriendship
from service.service_person import ServicePerson
from ui.user_interface import UserInterface


if __name__ == '__main__':
    repoPerson = RepoPerson()
    repoFriendship = RepoFriendship()

    srv_person = ServicePerson(repoPerson)
    srv_request = RepoRequest()
    srv_friendship = ServiceFriendship(repoFriendship)
    srv_notification = RepoNotification()
    ui = UserInterface(srv_person, srv_friendship, srv_request, srv_notification)
    ui.run()
