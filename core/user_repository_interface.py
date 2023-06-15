from abc import ABC, abstractmethod
from core.user import User


class UserRepositoryInterface(ABC):
    @abstractmethod
    def find_by_username(self, username: str) -> User:
        pass
