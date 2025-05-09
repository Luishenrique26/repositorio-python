from database.config import conection_db
from src.domain.entities.user_entity import UserEntity


class UserRepository:

    def get_user(self, username: str) -> dict | None:
        with conection_db() as cursor:
            query = cursor.execute(
            '''
                SELECT * FROM users WHERE username = ?
            ''', (username,)
            ).fetchone()
        return None if not query else {
            'user_id': query[0],
            'username': query[1],
            'password': query[2],
            'created_at': query[3]
        } 
    
    def create(self, entity: UserEntity) -> dict:
        with conection_db() as cursor:
            query = cursor.execute(
            '''
                INSERT INTO users (username, password, created_at) VALUES (?, ?, ?)
                RETURNING *
            ''', (entity.username, entity.password, entity.created_at)
            ).fetchone()
        return {
            'user_id': query[0],
            'username': query[1],
            'password': query[2],
            'created_at': query[3]
        }