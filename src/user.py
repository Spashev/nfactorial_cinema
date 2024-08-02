from .helpers import generate_id
from collections import namedtuple


class UserFabrica:
    __users = {}

    def addUser(self, user_name: str) -> str:
        user_id = generate_id()
        self.__users[user_id] = user_name
        return user_id

    def showAllUsers(self) -> None:
        print("# Вывод пользователей:")
        for user_id, user_name in self.__users.items():
            print(f"# {user_id}. {user_name.capitalize()}")
