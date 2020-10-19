import fastapi
from app import models, authenticate, exceptions

router = fastapi.APIRouter()


# ===============================================
# User APIs
# ===============================================
@router.get("/users")
def read_current_user(username: str = fastapi.Security(authenticate, scopes=["user_role"])):
    user_return = {"username": username, "age": 26}
    return user_return


@router.post("/users")
def register(user: models.User):
    raise exceptions.NotAllowedMethod()
