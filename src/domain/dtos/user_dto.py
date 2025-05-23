from dataclasses import dataclass
import re

@dataclass
class UserDTO:
    username: str
    email: str
    password: str

    @staticmethod
    def create(username: str, email: str, password: str) -> "UserDTO":
        return UserDTO(username, email, password)

    def validate(self) -> None:
        if not self.username:
            raise ValueError("Campo de nome de usuário obrigatório")

        if not self.email:
            raise ValueError("Campo de email obrigatório")

        if re.match(r'^\S+@\S+\.\S+$', self.email) is None:
            raise ValueError("Campo de email inválido")

        if not self.password:
            raise ValueError("Campo de senha obrigatória")

        if len(self.password) < 8:
            raise ValueError("O campo de senha deve ter pelo menos 8 caracteres")

        if self.username == self.password:
            raise ValueError(
                "O campo de senha deve ser diferente do campo de nome de usuário"
            )
