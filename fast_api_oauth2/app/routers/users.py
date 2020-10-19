import fastapi
from app import models, authenticate, exceptions
from app.services import users

router = fastapi.APIRouter()


# ===============================================
# User APIs
# ===============================================
@router.get("/users")
def read_current_user(username: str = fastapi.Security(authenticate, scopes=["user_role"])):
    return users.read_current_user(username)


@router.post("/users")
def register(user: models.User):
    raise exceptions.NotAllowedMethod()
