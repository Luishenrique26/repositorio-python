from dataclasses import dataclass

@dataclass
class UserDTO:
    username: str
    password: str
    
    @staticmethod
    def create(username: str, password: str) -> 'UserDTO':
        return UserDTO(username, password)
    
    def validate(self) -> None:
        if not self.username:
            raise ValueError('Username is required')
        if not self.password:
            raise ValueError('Password is required')
        if len(self.password) < 8:
            raise ValueError('Password must be at least 8 characters')