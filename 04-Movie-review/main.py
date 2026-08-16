from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables


@asynccontextmanager
async def lifespan(app:FastAPI):
    create_tables() # this is a file in database.py  just to add something
    print("Database tables created")

    yield
    print("shutting down the app")    


app = FastAPI(
    title="Movie Review Api",
    description="This is CRUD on Movie reviews implementing db",
    lifespan=lifespan
)

@app.get("/")
def home():
    return{
        "message":"Welcome to Movie Reviews"
    }




