import fastapi

from app import authenticate
from app.services import greetings

router = fastapi.APIRouter()


# ===============================================
# Hello APIs
# ===============================================
@router.get("/hello")
def hello_world():
    return {"message": "Hello World"}


@router.get("/hello/me")
def hello_me(username: str = fastapi.Security(authenticate, scopes=["user_role"])):
    return {"message": "Hello " + username}

