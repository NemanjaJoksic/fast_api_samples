import json

from src import models, exceptions, configs
import typing


# ==================================
# UserRepository implementations
# ==================================
class UserRepository:

    def add_user(self, user: models.User):
        raise NotImplementedError

    def get_user_by_username(self, username: str):
        raise NotImplementedError


class StaticUserRepository(UserRepository):

    def __init__(self) -> UserRepository:
        self.user = models.User(username=configs.security_username, password=configs.security_password)
        print('StaticUserRepository created')

    def add_user(self, user: models.User):
        raise exceptions.NotAllowedMethod

    def get_user_by_username(self, username: str):
        try:
            return self.user
        except KeyError:
            return None


class FileUserRepository(UserRepository):

    def __init__(self) -> UserRepository:
        with open('users.json') as file:
            users_list = json.load(file)
            self.users: typing.Dict[str, models.User] = {}
            for user in users_list:
                self.users[user["username"]] = models.User(username=user["username"], password=user["password"])

        print('FileUserRepository created')

    def add_user(self, user: models.User):
        raise exceptions.NotAllowedMethod

    def get_user_by_username(self, username: str):
        try:
            return self.users[username]
        except KeyError:
            return None


# =========================
# global variables
# =========================
user_repository: UserRepository = StaticUserRepository()
