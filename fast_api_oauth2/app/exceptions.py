import fastapi


class InvalidBasicCredentials(fastapi.HTTPException):

    def __init__(self):
        super().__init__(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"}
        )


class InvalidToken(fastapi.HTTPException):

    def __init__(self):
        super().__init__(
            status_code=405,
            detail="Invalid token"
        )


class NotAllowedMethod(fastapi.HTTPException):

    def __init__(self):
        super().__init__(
            status_code=405,
            detail="Not allowed method"
        )


