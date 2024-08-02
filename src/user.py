from .helpers import generate_id
from collections import namedtuple

User = namedtuple('User', ['id', 'name'])


class UserFabrica:
    __users = list()

    def addUser(self, user_name: str) -> User:
        user = User(generate_id(), user_name)
        self.__users.append(user)
        return user

    def showAllUsers(self) -> None:
        print("# Вывод пользователей:")
        for user in self.__users:
            print(f"# {user.id}. {user.name.capitalize()}")
