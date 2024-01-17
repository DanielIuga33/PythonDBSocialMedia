from repo.RepoPerson import RepoPerson
from service.ServicePerson import ServicePerson
from ui.UserInterface import UserInterface


if __name__ == '__main__':
    repo = RepoPerson("postgres", "12345678")
    srv = ServicePerson(repo)
    ui = UserInterface(srv)

    ui.run()
