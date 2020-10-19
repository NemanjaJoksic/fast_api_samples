import typing

import fastapi
import jwt

from app import exceptions, models

TOKEN_VALUE = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Ik5lbWFuamEgSm9rc2ljIiwidXNlcm5hbWUiOiJOZW1hbmphIiwicm9sZXMiOlsidXNlcl9yb2xlIiwiYWRtaXJfcm9sZSJdLCJzY29wZXMiOlsiZW1haWwiXSwianRpIjoiZWZlODNjMjUtMzNmZC00NDc3LTliZDUtNDM3NWE2MzJkZThmIiwiaWF0IjoxNjAzMTQxMTI2LCJleHAiOjE2MDMxNDQ4MDB9.KTbiN85WN9YBZ7FLi1_-4F1Hob5sVI4hlgWGnRJPUHc "


class TokenValidator:

    def validate(self, token: str) -> models.TokenDetails:
        raise NotImplementedError


class SimpleTokenValidator(TokenValidator):

    def __init__(self):
        self.__secret = "secret"
        self.__algorithm = ["HS256"]

    def validate(self, token: str) -> models.TokenDetails:
        print('SimpleTokenValidator validating token:' + token)
        try:
            decoded_token = jwt.decode(token, self.__secret, algorithms=self.__algorithm)
            token_details = models.TokenDetails(token=token, username=decoded_token["username"],
                                                roles=decoded_token["roles"], scopes=decoded_token["scopes"])
            return token_details
        except:
            print("Can't decode token")
            return None


def create_authenticate_oauth2() -> typing.Callable:
    # token schema
    oauth2_scheme = fastapi.security.OAuth2PasswordBearer(tokenUrl="token")
    # list of validators
    token_validators = [SimpleTokenValidator()]

    def authenticate_oauth2(security_scopes: fastapi.security.SecurityScopes, token: str = fastapi.Depends(oauth2_scheme)):
        token_details = None
        for token_validator in token_validators:
            token_details = token_validator.validate(token)
            if token_details is not None:
                break

        if token_details is None:
            raise exceptions.InvalidToken()

        print("token_details=" + token_details.json())
        print("required_scopes=" + str(security_scopes.scopes))
        return token_details.username

    return authenticate_oauth2
