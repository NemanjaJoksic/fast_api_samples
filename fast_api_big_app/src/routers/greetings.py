import fastapi

from src import authenticate


router = fastapi.APIRouter()


# ===============================================
# Hello APIs
# ===============================================
@router.get("/hello")
def hello_world():
    return {"message": "Hello World"}


@router.get("/hello/me")
def hello_me(username: str = fastapi.Depends(authenticate)):
    return {"message": "Hello " + username}

