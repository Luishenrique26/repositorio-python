from dataclasses import dataclass


@dataclass
class LoginDTO:
    username: str
    password: str

    @staticmethod
    def create(username: str, password: str) -> "LoginDTO":
        return LoginDTO(username, password)

    def validate(self) -> None:
        if not self.username:
            raise ValueError("Campo de nome de usuário obrigatório")

        if not self.password:
            raise ValueError("Campo de senha obrigatória")
