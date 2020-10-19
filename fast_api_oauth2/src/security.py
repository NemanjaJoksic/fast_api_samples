import typing

import fastapi

from src import exceptions


def create_authenticate_oauth2() -> typing.Callable:
    oauth2_scheme = fastapi.security.OAuth2PasswordBearer(tokenUrl="token")

    def authenticate_oauth2(security_scopes: fastapi.security.SecurityScopes, token: str = fastapi.Depends(oauth2_scheme)):
        print("token=" + token)
        print("scopes=" + str(security_scopes.scopes))
        if token != "111222333":
            raise exceptions.InvalidToken()
        return "Nemanja"

    return authenticate_oauth2
