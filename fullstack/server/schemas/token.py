from pydantic import BaseModel

class TokenBase(BaseModel):
    access_token: str
    token_type: str


class Token(TokenBase):
    username: str