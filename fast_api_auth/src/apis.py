import fastapi
from src import repositories, models, security

app = fastapi.FastAPI()
authenticate = security.get_authenticate()


# ===============================================
# Hello APIs
# ===============================================
@app.get("/hello")
def hello_world():
    return {"message": "Hello World"}


# ===============================================
# User APIs
# ===============================================
@app.get("/users")
def read_current_user(username: str = fastapi.Depends(authenticate)):
    user = repositories.user_repository.get_user_by_username(username)
    user_return = {"username": user.username, "age": user.age}
    return user_return


@app.post("/users")
def register(user: models.User):
    repositories.user_repository.add_user(user)
    return user
