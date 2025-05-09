from src.repositories.user_repository import UserRepository
from bcrypt import checkpw
class AuthService:
    def __init__(self) -> None:
        self.user_repository = UserRepository()

    def login(self, username: str, password: str) -> dict | None:
        user = self.user_repository.get_user(username)
        if not user:
            raise ValueError('User not found')
        
        if not checkpw(password.encode('utf-8'), user.get('password').encode('utf-8')):
            return ValueError('Password is incorrect')
        
        return user