import fastapi


router = fastapi.APIRouter()


# ===============================================
# Hello APIs
# ===============================================
@router.get("/hello")
def hello_world():
    return {"message": "Hello World"}

