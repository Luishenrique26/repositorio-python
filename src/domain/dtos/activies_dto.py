from dataclasses import dataclass
from datetime import datetime


@dataclass
class ActiviesDTO:
    name: str
    start_date: str | datetime
    end_date: str | datetime

    def validate(self) -> None:
        if not self.name:
            raise ValueError("Name is required")
        if not self.start_date:
            raise ValueError("Start date is required")
        if not self.end_date:
            raise ValueError("End date is required")
