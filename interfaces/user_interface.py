from abc import ABC, abstractmethod
from entities.user import User


class UserInterface(ABC):
    @abstractmethod
    def find_by_username(self, username: str) -> User:
        pass

    @abstractmethod
    def login(self, username: str, password: str) -> bool:
        pass

    @abstractmethod
    def register(self, username: str, password: str) -> bool:
        pass
