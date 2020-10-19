import fastapi

from src.routers import greetings, users


app = fastapi.FastAPI()

# add routers
app.include_router(greetings.router)
app.include_router(users.router)

