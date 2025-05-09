from src.repositories.user_repository import UserRepository
from src.domain.entities.user_entity import UserEntity
from src.domain.dtos.user_dto import UserDTO
from bcrypt import gensalt, hashpw
from random import randint

class UserService:
    def __init__(self) -> None:
        self.user_repository = UserRepository()

    
    def create_user(self, dto: UserDTO) -> dict:
        user_exists = self.user_repository.get_user(dto.username)
        
        if user_exists: 
            raise ValueError('User already exists')

        dto.password = hashpw(dto.password.encode('utf-8'), gensalt(rounds=randint(10,14))).decode('utf-8')
        entity = UserEntity.create(dto)
        return self.user_repository.create(entity)