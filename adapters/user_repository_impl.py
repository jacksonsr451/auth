from core.user import User
from core.user_repository_interface import UserRepositoryInterface


class UserRepositoryImpl(UserRepositoryInterface):
    def find_by_username(self, username: str) -> User:
        return User
