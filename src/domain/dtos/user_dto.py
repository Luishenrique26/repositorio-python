from dataclasses import dataclass


@dataclass
class UserDTO:
    username: str
    password: str

    @staticmethod
    def create(username: str, password: str) -> "UserDTO":
        return UserDTO(username, password)

    def validate(self) -> None:
        if not self.username:
            raise ValueError("Campo de nome de usuário obrigatório")
        if not self.password:
            raise ValueError("Campo de senha obrigatória")
        if len(self.password) < 8:
            raise ValueError("O campo de senha deve ter pelo menos 8 caracteres")

        if self.username == self.password:
            raise ValueError("Username and password must be different")
