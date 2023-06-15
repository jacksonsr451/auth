from abc import ABC, abstractmethod


class UserInterface(ABC):
    @abstractmethod
    def login(self, username: str, password: str) -> bool:
        pass

    @abstractmethod
    def register(self, username: str, password: str) -> bool:
        pass
