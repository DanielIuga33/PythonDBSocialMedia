from repo.repo_request import RepoRequest


class ServiceRequest:
    def __init__(self, repo: RepoRequest):
        self.__repo = repo

    def add(self, request):
        self.__repo.add(request)

    def delete(self, request):
        self.__repo.delete(request)

    def update(self, idc, request):
        self.__repo.update(idc, request)

    def get_all(self):
        return self.__repo.get_all()

    def size(self):
        return self.__repo.size()

