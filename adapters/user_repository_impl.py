from entities.user import User
from entities.user_repository_interface import UserRepositoryInterface


class UserRepositoryImpl(UserRepositoryInterface):
    def find_by_username(self, username: str) -> User:
        return User
