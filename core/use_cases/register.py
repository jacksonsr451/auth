from core.user_interface import UserInterface, UserRepositoryInterface


class RegisterUseCase(UserInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def register(self, username: str, password: str) -> bool:
        user = self.user_repository.find_by_username(username)
        if user:
            return False
        # TODO: Implementação para criar o novo usuário no banco de dados ou outra fonte de dados
        pass
