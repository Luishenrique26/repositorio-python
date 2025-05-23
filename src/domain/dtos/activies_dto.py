from dataclasses import dataclass
from datetime import date


@dataclass
class ActiviesDTO:
    name: str
    start_date: str | date
    end_date: str | date

    @staticmethod
    def create(
        name: str, start_date: str | date, end_date: str | date
    ) -> "ActiviesDTO":
        return ActiviesDTO(name, start_date, end_date)

    def validate(self) -> None:
        if not self.name:
            raise ValueError("Campo de nome de atividade é obrigatório")

        if not self.start_date:
            raise ValueError("Campo de data de inicio é obrigatório")

        if len(self.start_date) < 8 or len(self.start_date) > 8:
            raise ValueError("Campo de data de inicio é invalido")

        if not self.end_date:
            raise ValueError("Campo de data de fim é obrigatório")

        if len(self.end_date) < 8 or len(self.end_date) > 8:
            raise ValueError("Campo de data de fim é invalido")
