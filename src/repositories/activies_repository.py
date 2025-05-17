from database.config import conection_db
from src.domain.entities.activies_entity import ActiviesEntity


class ActiviesRepository:
    def get_activies(self):
        with conection_db() as cursor:
            query = cursor.execute(
                """
                SELECT * FROM activities
            """
            ).fetchall()
        return (
            None
            if not query
            else [
                {
                    "activitie_id": x[0],
                    "name": x[1],
                    "start_date": x[2],
                    "end_date": x[3],
                    "created_at": x[4],
                    "updated_at": x[5],
                }
                for x in query
            ]
        )

    def get_activie(self, name: str):
        with conection_db() as cursor:
            query = cursor.execute(
                """
                SELECT * FROM activities WHERE name = ?
            """,
                (name,),
            ).fetchone()
        return (
            None
            if not query
            else {
                "activitie_id": query[0],
                "name": query[1],
                "start_date": query[2],
                "end_date": query[3],
                "created_at": query[4],
                "updated_at": query[5],
            }
        )

    def create(self, entity: ActiviesEntity) -> dict:
        with conection_db() as cursor:
            query = cursor.execute(
                """
                INSERT INTO activities (name, start_date, end_date, created_at, updated_at) VALUES (?, ?, ?, ?, ?)
                RETURNING *
            """,
                (
                    entity.name,
                    entity.start_date,
                    entity.end_date,
                    entity.created_at,
                    entity.updated_at,
                ),
            ).fetchone()
        return {
            "activitie_id": query[0],
            "name": query[1],
            "start_date": query[2],
            "end_date": query[3],
            "created_at": query[4],
            "updated_at": query[5],
        }

    def update(self, entity: ActiviesEntity, id: int) -> dict:
        with conection_db() as cursor:
            query = cursor.execute(
                """
                UPDATE activities SET name = ?, start_date = ?, end_date = ?, updated_at = ? WHERE activitie_id = ?
                RETURNING *
            """,
                (
                    entity.name,
                    entity.start_date,
                    entity.end_date,
                    entity.updated_at,
                    id,
                ),
            ).fetchone()
        return {
            "activitie_id": query[0],
            "name": query[1],
            "start_date": query[2],
            "end_date": query[3],
            "created_at": query[4],
            "updated_at": query[5],
        }

    def delete(self, id: int):
        with conection_db() as cursor:
            query = cursor.execute(
                """
                DELETE FROM activities WHERE activitie_id = ?
                RETURNING *
            """,
                (id,),
            ).fetchone()
        return query
