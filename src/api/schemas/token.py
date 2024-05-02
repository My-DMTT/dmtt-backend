from uuid import UUID

from pydantic import BaseModel


class TokenSchema(BaseModel):
    access_token: str
    username: str
    # user_id: int


class TokenPayload(BaseModel):
    sub: str = None
    # exp: int = None
    jti: str


class UserOut(BaseModel):
    id: UUID
    email: str


class SystemUser(UserOut):
    password: str
