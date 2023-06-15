from core.user_interface import UserInterface, UserRepositoryInterface


class LoginUseCase(UserInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def login(self, username: str, password: str) -> bool:
        user = self.user_repository.find_by_username(username)
        if user and user.password == password:
            return True
        return False
