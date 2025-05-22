from src.domain.dtos import ActiviesDTO
from src.domain.entities import ActiviesEntity
from src.repositories import ActiviesRepository


class ActiviesService:
    def __init__(self) -> None:
        self.activies_repository = ActiviesRepository()

    def get_activies(self) -> list:
        return self.activies_repository.get_activies()

    def create_activie(self, dto: ActiviesDTO) -> dict:
        activie_exists = self.activies_repository.get_activie(dto.name)

        if activie_exists:
            raise ValueError("Activie already exists")

        entity = ActiviesEntity.create(dto)
        return self.activies_repository.create(entity)

    def update_activie(self, dto: ActiviesDTO, id: int) -> dict:
        activie_exists = self.activies_repository.get_activie(dto.name)

        if not activie_exists:
            raise ValueError("Activie not found")

        entity = ActiviesEntity.create(dto)
        return self.activies_repository.update(entity, id)

    def delete_activie(self, id: int) -> dict:
        return self.activies_repository.delete(id)
