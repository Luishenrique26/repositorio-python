from datetime import datetime
from src.domain.dtos.activies_dto import ActiviesDTO

class ActiviesEntity:
    def __init__(self, name: str, start_date: str, end_date: str, created_at: str, updated_at: str) -> None:
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.created_at = datetime.now() if not created_at else created_at
        self.updated_at = datetime.now()

    @staticmethod
    def create(dto: ActiviesDTO) -> 'ActiviesEntity':
        return ActiviesEntity(dto.name, dto.start_date, dto.end_date, dto.created_at)