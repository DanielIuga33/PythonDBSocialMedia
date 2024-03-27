from repo.repo_request import RepoRequest


class ServiceRequest:
    def __init__(self, repo: RepoRequest):
        self.__repo = repo

    def add(self, request):
        if self.find_request(request) != -1:
            raise Exception('Request already exists !')
        self.__repo.add(request)

    def delete(self, request):
        if self.find_request(request) == -1:
            raise Exception('Request does not exists !')
        self.__repo.delete(request)

    def delete_cascade(self, id_person):
        self.__repo.delete_cascade(id_person)

    def update(self, idc, request):
        self.__repo.update(idc, request)

    def get_all(self):
        return self.__repo.get_all()

    def size(self):
        return self.__repo.size()

    def find_request(self, elem):
        return self.__repo.find_request(elem)
