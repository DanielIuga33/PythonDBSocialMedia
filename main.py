from repo.repo_friendship import RepoFriendship
from repo.repo_notification import RepoNotification
from repo.repo_person import RepoPerson
from repo.repo_request import RepoRequest
from service.service_friendship import ServiceFriendship
from service.service_notification import ServiceNotification
from service.service_person import ServicePerson
from service.service_request import ServiceRequest
from ui.user_interface import UserInterface


if __name__ == '__main__':
    repoPerson = RepoPerson()
    repoRequest = RepoRequest()
    repoFriendship = RepoFriendship()
    repoNotification = RepoNotification()

    srv_person = ServicePerson(repoPerson)
    srv_request = ServiceRequest(repoRequest)
    srv_friendship = ServiceFriendship(repoFriendship)
    srv_notification = ServiceNotification(repoNotification)
    ui = UserInterface(srv_person, srv_friendship, srv_request, srv_notification)
    ui.run()
