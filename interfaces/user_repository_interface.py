from abc import ABC, abstractmethod
from entities.user import User


class UserRepositoryInterface(ABC):
    @abstractmethod
    def find_by_username(self, username: str) -> User:
        pass
