from repo.RepoFriendship import RepoFriendship
from repo.RepoPerson import RepoPerson
from service.ServicePerson import ServicePerson
from ui.UserInterface import UserInterface


if __name__ == '__main__':
    repoPerson = RepoPerson("postgres", "12345678")
    srv_person = ServicePerson(repoPerson)
    srv_friendship = RepoFriendship("postgres", "12345678")
    ui = UserInterface(srv_person, srv_friendship)

    ui.run()
