from datetime import datetime
from src.domain.dtos import ActiviesDTO
from datetime import datetime,date

class ActiviesEntity:
    def __init__(
        self,
        name: str,
        start_date: str,
        end_date: str,
    ) -> None:
        self.name = name
        self.start_date = date(
            day=int(start_date[0:2]), 
            month=int(start_date[2:4]), 
            year=int(start_date[4:8])
        )
        self.end_date = date(
            day=int(end_date[0:2]), 
            month=int(end_date[2:4]), 
            year=int(end_date[4:8])
        )
        self.created_at = datetime.now() 
        self.updated_at = datetime.now()

    @staticmethod
    def create(dto: ActiviesDTO) -> "ActiviesEntity":
        
        return ActiviesEntity(dto.name, dto.start_date.strip(), dto.end_date.strip())
