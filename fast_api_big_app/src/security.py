import secrets

import fastapi

from src import repositories, exceptions, configs


def create_authenticate_none():
    return lambda _: "anonymous"


def create_authenticate_basic():
    basic_security = fastapi.security.HTTPBasic()

    def authenticate_basic(credentials: fastapi.security.HTTPBasicCredentials = fastapi.Depends(basic_security)):
        user = repositories.user_repository.get_user_by_username(credentials.username)
        if user is None:
            raise exceptions.InvalidBasicCredentials

        correct_username = secrets.compare_digest(credentials.username, user.username)
        correct_password = secrets.compare_digest(credentials.password, user.password)
        if not (correct_username and correct_password):
            raise exceptions.InvalidBasicCredentials

        return credentials.username

    return authenticate_basic


def get_authenticate():
    if configs.security_type == "none":
        return create_authenticate_none()
    elif configs.security_type == "basic":
        return create_authenticate_basic()
    else:
        raise RuntimeError("Not supported authentication type " + configs.security_type)
