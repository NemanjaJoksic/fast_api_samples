import pydantic


class User(pydantic.BaseModel):
    username: str
    password: str
    age: int = None
