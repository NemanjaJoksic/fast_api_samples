import pydantic
import typing


class User(pydantic.BaseModel):
    username: str = pydantic.Field(default=None, alias="username")
    password: str = pydantic.Field(default=None, alias="password")
    age: int = pydantic.Field(default=None, alias="age")


class TokenDetails(pydantic.BaseModel):
    token: str = pydantic.Field(default=None, alias="token")
    username: str = pydantic.Field(default=None, alias="username")
    scopes: typing.List[str] = pydantic.Field(default=None, alias="scopes")
    roles: typing.List[str] = pydantic.Field(default=None, alias="roles")


