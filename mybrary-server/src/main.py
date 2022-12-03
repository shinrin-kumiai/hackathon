from fastapi import FastAPI

from src.dependencies import get_db
from src.routers import users, communities, books


app = FastAPI()
app.include_router(users.router)
app.include_router(communities.router)
app.include_router(books.router)


@app.get('/hello')
async def index() -> str:
    return "Hello world!"