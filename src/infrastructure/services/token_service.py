import random
from datetime import datetime, timedelta

import jwt
from passlib.context import CryptContext

from src.domain.constants import JWT_SECRET_KEY

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class TokenService():
    def __init__(self):
        self.SECRET_KEY = JWT_SECRET_KEY
        self.ALGORITHM = "HS256"
        self.ACCESS_TOKEN_EXPIRE_MINUTES = 120
        self.REFRESH_TOKEN_EXPIRE_MINUTES = 240

    def generate_verification_code(self) -> str:
        verification_code = ''.join(random.choices('0123456789', k=6))
        verification_code = '111111'
        return verification_code

    def create_access_token(self, user_id, jti) -> str:
        # expiration_time = datetime.now() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = {
            "sub": str(user_id),
            # "exp": expiration_time,
            "token_type": "access",
            "jti": str(jti)
        }
        return jwt.encode(to_encode, self.SECRET_KEY, self.ALGORITHM)

    def get_hashed_password(self, password: str) -> str:
        return password_context.hash(password)

    def verify_password(self, password: str, hashed_pass: str) -> bool:
        return password_context.verify(password, hashed_pass)
