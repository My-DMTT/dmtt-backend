from src.infrastructure.database.adapters.database import get_db
from src.infrastructure.models.auth import OtpCodes, SecurityJti
from src.infrastructure.models.user import User
from src.infrastructure.repositories.base import CRUDRepoBase


class JWTTokenRepo(CRUDRepoBase):
    model = SecurityJti

    async def get_user(self,  jti):
        with get_db() as session:
            return session.query(User).join(SecurityJti, SecurityJti.user_id == User.id).filter(SecurityJti.jti == jti).first()


class OtpCodesRepo(CRUDRepoBase):
    model = OtpCodes
